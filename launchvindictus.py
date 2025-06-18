from psutil import process_iter, Process
from os.path import dirname, join, getmtime, isfile
from datetime import datetime, timedelta
from os import system, environ
from time import sleep
from sys import argv, exit

# from InstallUEVR import get_uevr


def vindictus():
    for proc in process_iter():
        if proc.name() == "Vindictus.exe":
            if dirname(proc.exe()).endswith("Win64"):
                return proc.pid
    return 0


def vindictus_parent():
    for proc in process_iter():
        if proc.name() == "Vindictus.exe":
            if dirname(proc.exe()).endswith("Win64"):
                pass
            else:
                return proc.pid
    return 0


def black_cipher():
    for proc in process_iter():
        if proc.name() == "BlackCipher64.aes":
            return proc.pid
    return 0


def black_chk():
    for proc in process_iter():
        if proc.name() == "BlackXchg.aes":
            return proc.pid
    return 0


def loop():
    tries = 20
    while vindictus() == 0 and tries > 0:
        sleep(3)
        print("Waiting for vindictus to start")
        tries -= 1
    if vindictus() == 0:
        exit()
    print("Found vindictus")
    while vindictus() != 0:
        sleeptime = 10
        if len(argv) > 1:
            sleeptime = argv[1]
            print(
                f"Setting time between loops to commandline value {sleeptime} seconds (default 15)"
            )
        once = 1
        while once == 1:
            while black_chk() != 0:  # wait for startup process to end on its own
                print("Startup service found, waiting for it to end on its own")
                sleep(5)
            if black_cipher() != 0:
                sleep(6)  # need it to briefly startup to login
                Process(
                    black_cipher()
                ).terminate()  # I thought this was enough but then I started crashing with UUU and noticed it was getting respawned
                print("Killed black cipher")
                if vindictus_parent() != 0:
                    sleep(10)
                    Process(
                        vindictus_parent()
                    ).suspend()  # suspend parent process so it hopefully can't spawn more
            if black_cipher() == 0:  # now move to idle version
                once = 0
                # if not isfile(
                #     join(dirname(Process(vindictus).exe()), "uevr", "UEVRBackend.dll")
                # ):
                #     uevr = join(environ["APPDATA"], "UnrealVRMod", "UEVR")
                #     if (
                #         getmtime(backend := join(uevr, "UEVRBackend.dll")) < 1747969202
                #     ) or (
                #         datetime.now() - datetime.fromtimestamp(getmtime(backend))
                #     ) > timedelta(
                #         weeks=1
                #     ):
                #         print("Checking for UEVR updates")
                #         try:
                #             get_uevr()
                #         except Exception as e:
                #             pass
                #         sleep(4)
                #     print("starting UEVR")
                #     uevrinject = join(uevr, "UEVRInjector.exe")
                #     system(f'start "" {uevrinject} --attach=Vindictus.exe')

        while vindictus() != 0:
            if black_cipher() != 0:
                Process(black_cipher()).terminate()
            sleep(
                sleeptime
            )  # downside of this approach is obviously that a longer delay might fail to catch it
            # but since it only seems to attempt to restart occasionally and doesnt instantly crash this is just a small safety blanket
            # could use wmi and get an event triggered without an active process running but this is cheap enough to not care
    if vindictus_parent() != 0:
        Process(vindictus_parent()).terminate()
    exit()


if vindictus() == 0:
    system('start "" steam://rungameid/3576170/ -Windowed')
else:
    if black_cipher() != 0:
        Process(black_cipher()).terminate()
loop()
