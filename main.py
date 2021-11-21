import logging
import os
import re
import string
import subprocess
import sys
import zipfile
import contextlib

import requests
import argparse
from bs4 import BeautifulSoup


def check_for_swd_file():
    if sys.platform == "linux" or sys.platform == "linux2":  # linux
        if os.path.exists(os.path.join("resources", "swd")):
            return "swd"
        else:
            print("""
    Please go to this link: https://github.com/SegoCode/swd/releases and download the latest release of swd. 
    Place the file into the resources folder, rename it to swd and add the permission to execute.
    Then run the script again from the main folder
    """)
            sys.exit()
    elif sys.platform == "darwin":  # OS X
        sys.exit()  # MacOS is not supported atm
    elif sys.platform == "win32":  # Windows...
        if os.path.exists(os.path.join("resources", "swd.exe")):
            return "swd.exe"
        else:
            print("""
    Please go to this link: https://github.com/SegoCode/swd/releases and download the latest release of swd. 
    Place the file into the resources folder and rename it to swd.exe.
    Then run the script again from the main folder
    """)
            sys.exit()


def create_mod_folder(folder_name=None):
    if folder_name is None:
        folder_name = "mods1"
        while True:
            if os.path.exists(folder_name):
                iteration_number = str(int(folder_name[4:]) + 1)
                folder_name = folder_name[:4] + iteration_number
                continue
            os.mkdir(folder_name)
            break
    else:
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
    return folder_name


def return_mod_list_from_file(filepath):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
            lines = list(filter(lambda x: (x[0] != "#") and (x[0] not in string.whitespace), lines))
            lines = [line.strip() for line in lines]
    except FileNotFoundError:
        logging.error("The file specified does not exist.")
        sys.exit()
    if len(lines) == 0:
        logging.error("The mod list file is empty. Please update the file and try again")
        sys.exit()
    return lines


def download_mod_from_steam_workshop(swd_filename, link_or_code_to_mod):
    if link_or_code_to_mod.startswith("https://steamcommunity.com/sharedfiles/filedetails/?id="):
        mod_link = link_or_code_to_mod
    elif link_or_code_to_mod.isdecimal():
        mod_link = "https://steamcommunity.com/sharedfiles/filedetails/?id=" + link_or_code_to_mod
    else:
        logging.error("FAILED TO PARSE: {}".format(link_or_code_to_mod))
        return

    # Download the mod
    result_code = subprocess.call([os.path.join("..", "resources", swd_filename), mod_link])
    if result_code == 0:
        add_mod_id_to_completed_files_list(mod_link)
        return
    else:
        logging.warning("The download has failed")
        # Remove the incomplete file if present
        zip_file_name = "{}.zip".format(
            remove_prefix(mod_link, "https://steamcommunity.com/sharedfiles/filedetails/?id="))
        with contextlib.suppress(FileNotFoundError):
            os.remove(zip_file_name)


def get_mod_full_name(steam_mod_id):
    steam_mod_url = "https://steamcommunity.com/sharedfiles/filedetails/?id={}".format(steam_mod_id)
    page = requests.get(steam_mod_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get the name of the mod from steam main page
    name = soup.find("div", class_="workshopItemTitle").text
    name = name.replace(" ", "_")
    name = "".join([c for c in name if re.match(r'\w', c)])
    return name


def unpack_zip_files():
    files_in_directory = os.listdir(".")
    # Remove all non .zip files from the list
    files_in_directory = list(filter(lambda x: x.endswith(".zip"), files_in_directory))
    for archive_filename in files_in_directory:
        mod_full_name = get_mod_full_name(archive_filename)

        zf = zipfile.PyZipFile(archive_filename)
        zf.extract("contents.pak")
        os.rename("contents.pak", "{}-{}.pak".format(archive_filename[:-4], mod_full_name))
        os.remove(archive_filename)


def add_mod_id_to_completed_files_list(mod):
    mod = remove_prefix(mod, "https://steamcommunity.com/sharedfiles/filedetails/?id=")
    with open("completed_files.txt", "a") as file:
        file.write(mod + "\n")


def is_on_completed_files_list(mod):
    mod = remove_prefix(mod, "https://steamcommunity.com/sharedfiles/filedetails/?id=")
    if not os.path.exists("completed_files.txt"):
        return False
    with open("completed_files.txt", "r") as file:
        completed_files_ids = file.readlines()
    return True if mod in completed_files_ids else False


def remove_prefix(text, prefix):
    """You can remove this function in python 3.9.0"""
    return text[len(prefix):] if text.startswith(prefix) else text


def status_report(mod_list):
    missing_files = []
    mod_ids_list = [remove_prefix(mod, "https://steamcommunity.com/sharedfiles/filedetails/?id=") for mod in mod_list]
    with open("completed_files.txt", "r") as file:
        completed_mods_ids = list(map(str.strip, file.readlines()))

    logging.error("mod_ids_list: {}".format(mod_ids_list))
    logging.error("completed_mods_ids: {}".format(completed_mods_ids))
    for mod_id in mod_ids_list:
        if mod_id not in completed_mods_ids:
            missing_files.append(mod_id)

    if len(missing_files) == 0:
        logging.info("All files have been validated. Everything is OK.")
    else:
        logging.info("Some files are missing: ")
        for id in missing_files:
            logging.info(id)


def main(args):

    # Check if the "swd" (steam workshop downloader) file is present
    swd_filename = check_for_swd_file()
    logging.debug("SWD filename: {}".format(swd_filename))
    # Reads the file with mods and removes extra lines
    if args["input"]:
        mod_list = return_mod_list_from_file(args["input"])
    else:
        mod_list = return_mod_list_from_file("mod_list.txt")
    logging.debug("mod_list: {}".format(mod_list))

    if not args["check"]:
        # creates a new mod folder to save mods in
        if args["output"]:
            mod_folder_name = create_mod_folder(args["output"])
        else:
            mod_folder_name = create_mod_folder()
        os.chdir(mod_folder_name)
        # Download .zip files of the mods
        for modname in mod_list:
            if is_on_completed_files_list(modname):
                continue
            download_mod_from_steam_workshop(swd_filename, modname)
        unpack_zip_files()
        # Compare the mod list with the completed files
    status_report(mod_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Automatic downloader for Starbound mods')
    parser.add_argument("-c", "--check", action="store_true", help="Check if all mods are downloaded without downloading new ones")
    parser.add_argument("-o", "--output", help="Specifies the output folder")
    parser.add_argument("-i", "--input", help="Specifies the input mod list file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Turns on verbose mode")

    args = vars(parser.parse_args())
    if args["verbose"]:
        logging.basicConfig(level="DEBUG")
    else:
        logging.basicConfig(level="INFO")

    logging.debug("Arguments: {}".format(args))

    main(args)
