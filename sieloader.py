from utils import *
import subprocess

# first, searching for sierra
sierra_path = sierra_search()
addons_dir = "./addons/"

# second, check if addons folder exist, and if is, load addons from there
if os.path.isdir("./addons/"):
    addons = get_addons(addons_dir)
    # Now, lets check for install scripts
    for addon in addons:
        run_install_script(addons_dir, addon)

    # after we're done running installation scripts, we make universal addon file which user will load
    # and to make it easier, we will also open where file stored
    universal_addon_file = generate_addon_file(sierra_path, addons_dir, addons)
    subprocess.Popen([os.path.join(os.getenv('WINDIR'), 'explorer.exe'), '/select,', os.path.abspath(universal_addon_file)], start_new_session=True)
    subprocess.Popen([os.path.join(sierra_path, 'SIERRA.exe')], start_new_session=True)
else:
    os.mkdir("./addons/")