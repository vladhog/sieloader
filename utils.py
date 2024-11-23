import io
import os
if os.name == "nt":
    import winreg

import yaml


def sierra_search():
    sierra_path = None

    regs = [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]
    for i in regs:
        if sierra_path is None:
            aReg = winreg.ConnectRegistry(None, i)
            aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                                  0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
            count_subkey = winreg.QueryInfoKey(aKey)[0]
            for i in range(count_subkey):
                try:
                    asubkey_name = winreg.EnumKey(aKey, i)
                    asubkey = winreg.OpenKey(aKey, asubkey_name)
                    path, name = os.path.split(winreg.QueryValueEx(asubkey, "DisplayIcon")[0].split(",")[0])
                    if name == "SIERRA.exe":
                        sierra_path = path
                        break
                except Exception:
                    pass
        else:
            break
    return sierra_path


def get_addons(path):
    dirs = [x[1] for x in os.walk(path)][0]
    addon_dirs = []
    for i in dirs:
        if os.path.isfile(path + f"/{i}/addon.yaml"):
            addon_dirs.append(i)
    return dirs


def run_install_script(addons_dir, addon):
    try:
        with open(f"{addons_dir}/{addon}/install.txt") as file:
            data = [line.rstrip('\n') for line in file]
            for i in data:
                os.system(i)
    except Exception:
        pass


def generate_addon_file(addons_path, addons):
    paths = []
    scripts = []
    for addon in addons:
        paths.append(addons_path + f"{addon}")
        with open(addons_path + f"{addon}" + "/addon.yaml") as file:
            scripts += yaml.safe_load(file)['SCRIPTS']

    with io.open(f"sieloader_addons.yaml", 'w', encoding='utf8') as file:
        data = {"PATHS": paths, 'SCRIPTS': scripts}
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
    return f"sieloader_addons.yaml"
