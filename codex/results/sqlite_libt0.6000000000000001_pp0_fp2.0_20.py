import ctypes
import ctypes.util
import threading
import sqlite3
import os
import platform
import sys
import argparse
import subprocess
import datetime
import time
import re
import json
import shutil
import uuid
import random
import string
import tempfile

# change the path to the directory where the executable is
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_path, "..", "common"))
sys.path.append(os.path.join(base_path, "..", "common", "win32"))

import util
import win32
import win32.win32con
import win32.win32gui
import win32.win32api
import win32.win32process
import win32.win32event
import win32.win32file
import win32.win32security
import win32.win32pipe


# change this if the program is not in the same directory as the script
executable_path = os.path.join(base_path, "..", "..", "bin", "wireshark.
