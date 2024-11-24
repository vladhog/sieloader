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
    if os.name == "nt":
        subprocess.Popen([os.path.join(os.getenv('WINDIR'), 'explorer.exe'), '/select,', os.path.abspath(universal_addon_file)], start_new_session=True)
        subprocess.Popen([os.path.join(sierra_path, 'SIERRA.exe')], start_new_session=True)
    else:
        showinfo('Thank you for using sieloader', 'Your universal addon file is ready, you can find it in sieloader program folder called sieloader_addons.yaml. Thank you for using sieloader!')
else:
    os.mkdir(addons_dir)
