import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') for write-only in-memory use
import os, sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
import gettext
import time

# Local imports
from . import misc, settings, logger, config, comar, util

__all__ = ["PackageKitGTK"]

class PackageKitGTK(object):
    def __init__(self, parent=None, root=True, uid=None):
        ### Initilize gettext
        #gettext.install("package-manager", "/usr/share/locale")
        gettext.bindtextdomain("package-manager", "/usr/share/locale")
        gettext.textdomain("package-manager")
        self.appName = "package-manager"
        self.localedir = "/usr/share/locale"

        # Set root or user mode
        self.root = root
        self.uid =
