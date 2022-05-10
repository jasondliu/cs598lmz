import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import stat
import sys

if sys.platform == 'darwin':
    import objc
    import Foundation
    import AppKit
    import CoreFoundation

else:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, GObject
    from gi.repository.GLib import Variant

import dbus
import dbus.service
import dbus.mainloop.glib

import xml.etree.ElementTree as ET

from . import common
from . import config
from . import xdg

def get_dbus_object(bus, name, path):
    return bus.get_object(name, path)

def get_dbus_property(bus, name, path, iface, prop):
    obj = get_dbus_object(bus, name, path)
    return dbus.Interface(obj, dbus.PROPERTIES_IFACE).Get(iface, prop)

