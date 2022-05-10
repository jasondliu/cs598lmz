import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import dbus
import dbus.service
import dbus.mainloop.glib
import webbrowser
import pygame
from gi.repository import GObject
import os

# This is the path to the sqlite database that contains
# information about the iDevices and their paired hosts
DEVICES_DB = os.environ['HOME'] + '/.config/obexd/devices.conf'

# This is the path to the sqlite database that contains
# information about the search records
SEARCH_DB = os.environ['HOME'] + '/.cache/gnome-bluetooth/search.db'

# This is the path to the sqlite database that contains
# information about the discovered devices
DISCOVERED_DB = os.environ['HOME'] + '/.cache/gnome-bluetooth/discovered.db'

# This is the path to the sqlite database that contains
# information about the connections
CONNECTIONS_DB = os.environ['HOME'] + '/.cache/gnome-bluetooth/connections.db'

