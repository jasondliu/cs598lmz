import ctypes
import ctypes.util
import threading
import sqlite3
import time

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GdkX11', '3.0')

from gi.repository import Gtk, GdkX11

from . import config

class SettingsDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Settings", parent, 0)
        self.set_default_size(150, 100)

        box = self.get_content_area()

        self.entry = Gtk.Entry()
        box.add(self.entry)

        self.show_all()

class Entry(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Entry")
        self.set_default_size(300, 300)
        self.connect("delete-event", Gtk.main_quit)
        self.connect("focus-out-event", self.focus_out)

