from utils import *
import subprocess

# first, searching for sierra
sierra_path = sierra_search()
addons_dir = sierra_path + "/addons/"

# second, check if addons folder exist, and if is, load addons from there
if os.path.isdir(sierra_path + "/addons/"):
    addons = get_addons(addons_dir)
    # Now, lets check for install scripts
    for addon in addons:
        run_install_script(addons_dir, addon)

    # after we're done running installation scripts, we make universal addon file which user will load
    # and to make it easier, we will also open where file stored
    universal_addon_file = generate_addon_file(sierra_path, addons_dir, addons)
    subprocess.run([os.path.join(os.getenv('WINDIR'), 'explorer.exe'), '/select,', os.path.abspath(universal_addon_file)])
    subprocess.run([os.path.join(sierra_path, 'SIERRA.exe')])
else:
    os.mkdir(sierra_path + "/addons/")