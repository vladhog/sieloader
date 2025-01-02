from utils import *
import subprocess
import os
from tkinter.messagebox import showinfo

# first, searching for sierra
# If we are working on linux, then we don't need sierra path
if os.name == "nt":
    sierra_path = sierra_search()
else:
    sierra_path = None

sierra_config_path = os.path.expanduser("~") + "/SIERRA_CONF.json"
addons_dir = f"{os.getcwd()}/addons/"

# second, check if addons folder exist, and if is, load addons from there
if os.path.isdir(addons_dir):
    addons = get_addons(addons_dir)
    # Now, lets check for install scripts
    for addon in addons:
        run_install_script(addons_dir, addon)

    # after we're done running installation scripts, we make universal addon file which user will load
    # and to make it easier, we will also open where file stored
    universal_addon_file = generate_addon_file(addons_dir, addons)
    edit_sierra_config(sierra_config_path, universal_addon_file)
    if os.name == "nt":
        subprocess.Popen([os.path.join(sierra_path, 'SIERRA.exe')], start_new_session=True)
    else:
        showinfo('Thank you for using sieloader', 'Your universal addon file is ready, SIERRA configured to lunch it on next start. Thank you for using sieloader!')
else:
    os.mkdir(addons_dir)
