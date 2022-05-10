import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import subprocess
import locale
import re

# Define some constants

TRAY_ICON_PATH = os.path.join(os.path.dirname(__file__), 'icon.png')

# Define some variables

app = None
tray_icon = None
tray_menu = None
tray_menu_exit = None
tray_menu_open = None
tray_menu_separator = None
tray_menu_show_hide = None
tray_menu_show_hide_label = None
tray_menu_update_now = None
tray_menu_update_now_label = None
tray_menu_update_now_separator = None
tray_menu_update_now_separator_2 = None
tray_menu_update_now_separator_3 = None
tray_menu_update_now_separator_4 = None
tray_menu_update_now_separator_5 = None
tray_menu_update_now_separator_6 = None

