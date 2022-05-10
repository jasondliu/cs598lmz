import ctypes
ctypes.windll.user32.SetProcessDPIAware()
import os
import sys
import time
import logging
import json
import base64
import itertools
import glob
import shutil
import datetime
import subprocess
import traceback
import threading
import requests
import webbrowser
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk

# Get the path to the assets folder
ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

# Import the PyInstaller bootloader modules
import pyimod03_importers
import pyimod04_archive
import pyimod05_code
import pyimod06_boot_common
import pyimod07_machinery
import pyimod08_archive
import pyimod09_crypto_none
import pyimod10_carchive
import pyimod11_carchive

# Extract the PyInstaller bootloader
pyi_bootstrap_
