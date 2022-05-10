import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess
import re
import datetime
import shutil
import json
import string
import random
import traceback

# Import the Python bindings for Avahi
try:
    import dbus
    import avahi
    import dbus.glib
except ImportError:
    print "Avahi Python bindings not found. Please install python-avahi"
    sys.exit(1)

# Import the Python bindings for GObject
try:
    import gobject
except ImportError:
    print "GObject Python bindings not found. Please install python-gobject"
    sys.exit(1)

# Import the Python bindings for libnotify
try:
    import pynotify
except ImportError:
    print "libnotify Python bindings not found. Please install python-notify"
    sys.exit(1)

# Import the Python bindings for the GTK+ toolkit
try:
    import pygtk
    import gtk
    import gtk.glade
except ImportError:
    print "GTK+ not found. Please install python-
