import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys

# python-gobject from jhbuild
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkX11', '3.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkX11
from gi.repository import WebKit
from gi.repository import GLib

# pysqlcipher
import pysqlcipher.dbapi2

class App(Gtk.Window):
    def __init__(self, url):
        Gtk.Window.__init__(self)
        self.set_title("Mygtk")
        self.set_size_request(300, 400)
        self.set_border_width(5)
        self.set_position(Gtk.WindowPosition.CENTER)
