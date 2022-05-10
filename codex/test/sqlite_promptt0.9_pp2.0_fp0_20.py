import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file:" + '/../test.db' + "?mode=ro", uri=True)
import sys
import os
import time
import re
import platform
import subprocess
from glob import glob
import shutil
import json
from collections import OrderedDict

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from cefpython3 import cefpython as cef
from cef_settings import CefSettings

from .uis.ui_mainwindow import Ui_MainWindow
from .uis import ui_about, ui_newtab
from .uis.ui_notification import Ui_Notification

from . import modules
from . import options

# Some constants.
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_DIR = CURRENT_DIR + "/../../tests"
TEST_MESSAGE = "Hello CefPython!"
BROWSER_BACK = "<"
