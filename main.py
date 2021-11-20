import sys, os, subprocess, re, string, zipfile
from bs4 import BeautifulSoup
import requests


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

def create_mod_folder():
    folder_name = "mods1"
    while True:
        if os.path.exists(folder_name):
            iteration_number = str(int(folder_name[4:]) + 1)
            folder_name = folder_name[:4] + iteration_number
            continue
        os.mkdir(folder_name)
        break
    return folder_name

def return_mod_list_from_file():
    with open("mod_list.txt", "r") as file:
        lines = file.readlines()
        lines = list(filter(lambda x: (x[0] != "#") and (x[0] not in string.whitespace), lines))
        return lines

def download_mod_from_steam_workshop(swd_filename, link_or_code_to_mod):
    if link_or_code_to_mod.startswith("https://steamcommunity.com/sharedfiles/filedetails/?id="):
        pass
    elif link_or_code_to_mod.isdecimal():
        link_or_code_to_mod = "https://steamcommunity.com/sharedfiles/filedetails/?id=" + link_or_code_to_mod
    else:
        print("FAILED TO PARSE: {}".format(link_or_code_to_mod))
        return
    subprocess.call(["pwd"])
    subprocess.call([os.path.join("..", "resources", swd_filename), link_or_code_to_mod])

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


def main():
    # Check if the "swd" (steam workshop downloader) file is present
    swd_filename = check_for_swd_file()
    # creates a new mod folder to save mods in
    mod_folder_name = create_mod_folder()
    # Reads the file with mods and removes extra lines
    mod_list = return_mod_list_from_file()
    os.chdir(mod_folder_name)
    # Downloads .zip files of the mods
    for modname in mod_list:
        download_mod_from_steam_workshop(swd_filename, modname)
    unpack_zip_files()


if __name__ == "__main__":
    main()
