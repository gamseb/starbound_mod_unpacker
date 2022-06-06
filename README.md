This is a simple Starbound mod downloader and unpacker
# Requirements:
- Python 3
- [Beautiful soup 4](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup)

# How to use: 
1. Download or clone the repository
2. Go to https://github.com/SegoCode/swd/releases and download the latest release for your operating system (Usually its either swd-linux-386 or swd-windows-386.exe)
3. Put the file into the **resources/** folder
> If on Linux, remember to add the correct permissions to the **swd** binary
4. Make sure you have Python 3 installed
5. Install Beautiful soup 4 by running the following command in the terminal:
> $ python3 -m pip install bs4
6. Write your mod list into the **mod_list.txt** file
7. run **main.py** with the following command in the terminal and wait for all the mods to finish downloading:
> $ python3 main.py

# Options

Check if all mods are downloaded without downloading new ones. Needs path to the completed_files.txt file
> $ python3 main -c 
 
Specifies the output folder (can be used to resume downloads or update colections with new mods)
> $ python main -o (folder name)
  
Specifies the input mod list file
> $ python main -i (txt file)

Turns on verbose mode
> $ python main -v


# Mod list example: 

```
#######
# Content mods
#######
# Frackin universe
https://steamcommunity.com/sharedfiles/filedetails/?id=729480149
# Elithian races mod
https://steamcommunity.com/sharedfiles/filedetails/?id=850109963
# Avali (Triage) Race Mod
https://steamcommunity.com/sharedfiles/filedetails/?id=729558042
# Customizable shuttlecraft
https://steamcommunity.com/sharedfiles/filedetails/?id=1102394541
# Enhanced storage
https://steamcommunity.com/sharedfiles/filedetails/?id=731220462
# The Saturnians
https://steamcommunity.com/sharedfiles/filedetails/?id=1103027918
# The Kyterrans
https://steamcommunity.com/sharedfiles/filedetails/?id=2280798282
# The Starforge
https://steamcommunity.com/sharedfiles/filedetails/?id=2431875552
# Anom's Outpost Overhaul
https://steamcommunity.com/sharedfiles/filedetails/?id=2468903056
# Scyphojel, Space Jellyfish!
https://steamcommunity.com/sharedfiles/filedetails/?id=2655101811
# Arcana
# https://steamcommunity.com/sharedfiles/filedetails/?id=2359135864
# Macrochips
https://steamcommunity.com/sharedfiles/filedetails/?id=729444820


#######
# Fixes
#######
# Avali FU fix
https://steamcommunity.com/sharedfiles/filedetails/?id=2052758462
# Xbawks Character Extender
https://steamcommunity.com/sharedfiles/filedetails/?id=729426722
# [OFFICIAL] FU BYOS Modded Race Patch
https://steamcommunity.com/sharedfiles/filedetails/?id=1194878261
# More Outpost Objects
https://steamcommunity.com/sharedfiles/filedetails/?id=1635522739
# More Teleportz
https://steamcommunity.com/sharedfiles/filedetails/?id=1543782525
# Outpost Nebula - Pillars of Creation
https://steamcommunity.com/sharedfiles/filedetails/?id=957095453
# Hope on shops 
https://steamcommunity.com/sharedfiles/filedetails/?id=960708990
# Anom's Outpost Overhaul - Enhanced Storage Patch
https://steamcommunity.com/sharedfiles/filedetails/?id=2468895859
# Outpost Shuttlecraft
https://steamcommunity.com/sharedfiles/filedetails/?id=1114277962
# Anom's Outpost Overhaul - Outpost Shuttlecraft Patch
https://steamcommunity.com/sharedfiles/filedetails/?id=2468896108
# Elithian Ship Backgrounds
https://steamcommunity.com/sharedfiles/filedetails/?id=933536396
# Frackin' Universe - Elithian BYOS Ships
https://steamcommunity.com/sharedfiles/filedetails/?id=2375270402
# Elithian Races Mod: Frackin Universes Patch
https://steamcommunity.com/sharedfiles/filedetails/?id=1429652829
# Macrochip fix
https://steamcommunity.com/sharedfiles/filedetails/?id=1923815089
# bk3k's Inventory Reskin
https://steamcommunity.com/sharedfiles/filedetails/?id=1150594604


######
# QOL improvements
######
# Compact crops for FU
https://steamcommunity.com/sharedfiles/filedetails/?id=2265144528
# Compact Crops: Lumen Plants from The Saturnians
https://steamcommunity.com/sharedfiles/filedetails/?id=2385914603
# Extra zoom modes
https://steamcommunity.com/sharedfiles/filedetails/?id=729791646
# Frackin interface
https://steamcommunity.com/sharedfiles/filedetails/?id=1264107917
# Scripted Artificial Intelligence Lattice (Customisable A.I.!)
https://steamcommunity.com/sharedfiles/filedetails/?id=947429656
# Frackin' Action Bars
https://steamcommunity.com/sharedfiles/filedetails/?id=821455287
# Skippable cinematics 
https://steamcommunity.com/sharedfiles/filedetails/?id=729428037
# No Highlights On Inspected Objects
https://steamcommunity.com/sharedfiles/filedetails/?id=2511429674
# Buy Outpost Shops
https://steamcommunity.com/sharedfiles/filedetails/?id=1103637589
# Container UI Tweak
https://steamcommunity.com/sharedfiles/filedetails/?id=729524482
# Anom's Outpost Overhaul - Scrap Vendor Addon
https://steamcommunity.com/sharedfiles/filedetails/?id=2478120319
# Planet navigation tools
https://steamcommunity.com/sharedfiles/filedetails/?id=2613620322
# bk3k's Inventory: extended inventory 
https://steamcommunity.com/sharedfiles/filedetails/?id=882900100
# Food Stack
https://steamcommunity.com/sharedfiles/filedetails/?id=729427436
# Disabled items drop in survival
https://steamcommunity.com/sharedfiles/filedetails/?id=729746228
# Improved Food Descriptions
https://steamcommunity.com/sharedfiles/filedetails/?id=731354142
# Instant crafting
https://steamcommunity.com/sharedfiles/filedetails/?id=729427744


######
# Misc
######
# CrazyFreak's Musical Collection
https://steamcommunity.com/sharedfiles/filedetails/?id=729773633
# Frackin music
https://steamcommunity.com/sharedfiles/filedetails/?id=729492703
# Outpost Music Replacer: Tranquility Base
https://steamcommunity.com/sharedfiles/filedetails/?id=1826459917
