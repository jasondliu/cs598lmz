import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

from gi.repository import GLib
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject, Gedit

APP_ID = "org.gnome.gedit.plugins.GeditLangTool"

# add path to LT_HOME if LT_HOME is not set and python-languagetool is not in sys.path
LT_HOME = os.environ.get('LT_HOME', None)

if LT_HOME is not None:
    LT_PATH = LT_HOME
elif LT_HOME is None:
    LT_PATH = os.path.split(__file__)[0]
else:
    LT_PATH = ''

if LT_PATH not in sys.path:
    sys.path.append(LT_PATH)

try:
    import LanguageTool
    LT_AVAILABLE = True
except ImportError:
    print("LanguageTool:  python-languagetool is not installed")
    LT_AVAILABLE = False

try:
    from
