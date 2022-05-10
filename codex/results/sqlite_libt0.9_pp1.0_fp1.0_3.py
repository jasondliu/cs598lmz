import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import os
import ConfigParser
import shutil
import subprocess
import time
import glob
import platform

config = ConfigParser.ConfigParser()
configFile = "config.ini"
# Check if config file exists, if it doesn't we create one
if(os.path.isfile(configFile) == False):
    config.add_section("Settings")
    config.add_section("Paths")
    config.set("Settings", "project", "")
    config.set("Settings", "version", "")
    config.set("Paths", "prefProj", "")
    config.set("Paths", "gamedir", "")
    config.set("Paths", "prefPath", "")
    config.set("Paths", "exedir", "")
    config.set("Paths", "passConfig", "")
    config.set("Paths", "manifestdir", "")

    with open(configFile, "w+") as configfile:
        config.write(configfile)

# Run config file
config
