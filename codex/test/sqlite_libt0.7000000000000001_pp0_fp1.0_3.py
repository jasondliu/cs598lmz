import ctypes
import ctypes.util
import threading
import sqlite3

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
gi.require_version("GdkPixbuf", "2.0")
from gi.repository import Gtk, Gdk, GdkPixbuf

import dbus
import dbus.service
import dbus.mainloop.glib

import gettext
gettext.install("alarm-clock", "/usr/share/locale", names="ngettext")

# We use a single global variable for the application object.  If a
# thread wants to access this object, we have to lock it first.
app = None
app_lock = threading.Lock()

# The user's home directory.
home = os.getenv("HOME")

# The user's face.
face = home + "/.face"

# The user's alarm-clock configuration directory.
config_dir = home + "/.config/alarm-clock"

# File name for the alarm database.
