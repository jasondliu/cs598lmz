import mmap
import os
import re
import sys
import stat
import shutil
import fileinput
import datetime
import subprocess
import yaml

# Configuration

# Path to the project to be built
project_path = os.path.join(os.path.dirname(__file__), "../", "..")

# May be "Debug", "DebugAndroid", "Release"
# For building on the desktop Debug and Release work, DebugAndroid works on Android
android_build_configuration = "DebugAndroid"

# Path to where the build will be deployed.
# Use absolute path, i.e. /home/vividos/games/yourgame
# If you are using Linux Mint, Unity will create a new
# .config folder in your home directory, so your game's data will be in
# /home/vividos/.config/yourgame
android_deploy_path = "/home/vividos/games/yourgame"

# Path to where the build will be deployed.
# Use absolute path, i.e. /home/vividos/games/yourgame
# If you are using
