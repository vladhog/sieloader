# SIERRA addons loader
With this program it will be simple to load ton of addons at same time, just put them in folder and after SIERRA run, choose sieloader addon file that will be selected in explorer

# Installation
1. Download archive from [releases](https://github.com/vladhog/sieloader/releases) according to your os.
2. Unpack archive
3. Done! Lunch sieloader.exe or sieloader.bin inside folder. Nothing complicated.

# Addons structure 
```
- SIERRA root directory
    - /addons
        - /myaddon
            - install.txt
            - addon.yaml
            - myaddon.py
            - /anothermyaddon
                - moreaddons.py
```
# How it works
1. We search for sierra root folder
2. Load addons from /addons folder
3. Run their installation scripts from install.txt (each line being executed in cmd)
4. Making one invoker out of all addon files
5. Done! You can load sieloader_addons.yaml from SIERRA root directory and all your addons will work!

# License
Sieloader © 2024 by Vladhog Security is licensed under Attribution-NonCommercial-ShareAlike 4.0 International.
