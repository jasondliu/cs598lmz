import ctypes
import ctypes.util
import threading
import sqlite3

from gi.repository import GObject, Gtk, Gdk, Gedit, PeasGtk

class BBDBPlugin(GObject.Object, Gedit.WindowActivatable, PeasGtk.Configurable):
    __gtype_name__ = "BBDBPlugin"

    dirty = GObject.property(type=bool, default=False)
    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)
        self.dirty = False
        self.window = None

    def do_activate(self):
        self.window.set_data('BBDBPluginInfo', self)

        self.insert_menu()
        self.insert_context_menu()

    def do_deactivate(self):
        self.remove_menu()
        self.remove_context_menu()

        self.window.set_data('BBDBPluginInfo', None)

