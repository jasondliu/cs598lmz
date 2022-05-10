import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess
import json
import datetime
import shutil

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")

from gi.repository import Gtk, Gdk, GLib
from gi.repository import GObject

# libnotify
try:
    import notify2
    notify2.init("Gnote")
except ImportError:
    notify2 = None

# pynotify
try:
    import pynotify
    pynotify.init("Gnote")
except ImportError:
    pynotify = None

# win32
try:
    import win32api
    import win32con
    import win32gui
    import win32process
    import win32security
    import win32ui
    import win32event
    import win32gui_struct
    import pywintypes
except ImportError:
    win32api = None

# xlib
try:
    from Xlib.display import Display
