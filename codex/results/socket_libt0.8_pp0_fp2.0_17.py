import socket
import time
import os
import sys

# set emulator
os.environ['ANDROID_HOME'] = "C:\Archivos de programa\Android\android-sdk"
os.environ['ANDROID_SDK_ROOT'] = "C:\Archivos de programa\Android\android-sdk"
os.environ['ANDROID_AVD_HOME'] = "C:\Archivos de programa\Android\android-sdk\avd"

# set phone
os.environ['ANDROID_SERIAL'] = "C1D6JKWMJ8"


def start_emulator():
    # get devices ids
    devices_ids = list(map(lambda x: x[8:], subprocess.check_output(["adb", "devices"]).decode().splitlines()))

    # verify devices ids empty
    if len(devices_ids) != 0:
        if devices_ids[0] != "":
            print("is not possible to start the emulator. Remove the connected devices")
            sys.exit(0
