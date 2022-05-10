import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import gtk
import gobject
import pango
import re
import sys

try:
    import pynotify
    pynotify.init("Pidgin")
except:
    pynotify = None

try:
    import dbus
    import dbus.service
    import dbus.mainloop.glib
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
except:
    dbus = None

import purple

# For some reason, the Python bindings for dbus-python don't include
# dbus.UInt32.  However, the low-level bindings do, so we can just use
# that instead.
dbus_introspection = ctypes.CDLL(ctypes.util.find_library('dbus-1'))
dbus_introspection.dbus_uint32_t = ctypes.c_uint32

# Purple doesn't seem to define PURPLE_PLUGINS
PURPLE_PLUGINS = 1

# This is the version of the plugin
