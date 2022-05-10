import ctypes
import ctypes.util
import threading
import sqlite3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject

from . import config

def get_libc():
    """Return the ctypes libc object."""
    libc_path = ctypes.util.find_library('c')
    if not libc_path:
        raise OSError('libc not found')
    return ctypes.CDLL(libc_path)

class DBus(object):
    """DBus interface for the daemon."""
    def __init__(self, daemon):
        self.daemon = daemon
        self.libc = get_libc()
        self.dbus = self.libc.dbus_bus_get(self.libc.DBUS_BUS_SYSTEM, None)
        self.connection = self.libc.dbus_connection_open_private(
            self.dbus, None)
