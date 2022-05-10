import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import pprint
pp = pprint.PrettyPrinter(indent=4)

from PyQt4 import QtCore, QtGui
from qt4_utils import *
from GConf import GConf
from player import Player
from playlist import Playlist
from treeview import TreeView
from status import Status
from tray import Tray
from controls import Controls
from config import Config

from mpris import Mpris

import messages
from messages import *

from os.path import join, dirname, abspath, expanduser

try:
    from pynotify import init as notify_init, Notification
    from pynotify import URGENCY_LOW, URGENCY_NORMAL, URGENCY_CRITICAL
except ImportError:
    notify_init = None

from dbus.mainloop.glib import DBusGMainLoop

from dbus.glib import threads_init
from dbus.glib import init_threads
from dbus.glib import DBusGMainLoop
from dbus import glib
from dbus import SessionBus
