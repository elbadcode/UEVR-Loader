from os import system, chdir, environ, scandir, remove
from os.path import *
from sys import argv
import requests
from shutil import unpack_archive


def get_uevr():
    contents = [
        "openxr_loader.dll",
        "revision.txt",
        "UEVRBackend.dll",
        "UEVRBackend.pdb",
        "UEVRInjector.dll.config",
        "UEVRInjector.exe",
        "UEVRInjector.pdb",
        "UEVRPluginNullifier.dll",
        "LuaVR.dll",
        "openvr_api.dll",
    ]

    url = f"https://api.github.com/repos/praydog/uevr-nightly/releases/latest"
    headers = {"Accept": "application/vnd.github.inertia-preview+json"}
    r = requests.get(url, headers=headers)
    dl = r.json()["assets"][0]["browser_download_url"]
    chdir(uevr := join(environ["appdata"], "UnrealVRMod"))
    with open("uevrlatest.zip", "wb") as f:
        f.write(requests.get(rf"{str(dl)}").content)
        f.close()
    files = [
        f.path for f in scandir(join(uevr, "UEVR")) if f.name.endswith(tuple(contents))
    ]
    for file in files:
        if isfile(file):
            remove(file)
    unpack_archive(uevrf := join(uevr, "uevrlatest.zip"), "UEVR")
    system(join(uevrf, "UEVRInjector.exe"))


if len(argv) == 1:
    get_uevr()
