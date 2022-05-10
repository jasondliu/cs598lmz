import mmap
import os
import sys
import platform
import subprocess
import re
import psutil
import tempfile
import threading
import time
import keyboard
import webbrowser
import pyautogui
import ctypes
import socket
import colorama


#---------
# Globals
#---------

FNULL = open(os.devnull, 'w')

# Colors
N = '\033[0m'    # normal
R = '\033[31m'   # red
G = '\033[32m'   # green
O = '\033[33m'   # orange
B = '\033[34m'   # blue
P = '\033[35m'   # purple
C = '\033[36m'   # cyan
GR = '\033[37m'  # gray
T = '\033[93m'   # tan

INFO = '\033[94m'

# Misc
RUNNING_OS = platform.system()

# Paths
#ROOT_DIR = os.path.dirname(os.path.realpath(__
