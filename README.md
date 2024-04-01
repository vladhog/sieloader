# SIERRA addons loader
With this program it will be simple to load ton of addons at same time, just put them in folder and after SIERRA run, choose sieloader addon file that will be selected in explorer

# Addons structure 
```
- SIERRA root directory
    - /addons
        - /myaddon
            - install.txt
            - addon.yaml
            - myaddon.py
```
# How it works
1. We search for sierra root folder
2. Load addons from /addons folder
3. Run their installation scripts from install.txt
4. Making one invoker out of all addon files
5. Done! You can load sieloader_addons.yaml from SIERRA root directory and all your addons will work!
