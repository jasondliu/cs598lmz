import ctypes
import ctypes.util
import threading
import sqlite3
import os

import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GObject
from gi.repository import GLib

from . import rss

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

class Updater(dbus.service.Object):
    def __init__(self, bus, object_path):
        dbus.service.Object.__init__(self, bus, object_path)
        self.updating = False
        self.last_update = 0
        self.db = sqlite3.connect('/home/nadir/rss.db')

    def update(self):
        if not self.updating:
            self.updating = True
            self.last_update = int(time.time())
            self.thread = threading.Thread(target=self.do_update)
            self.thread.start()

    @dbus.service.method(dbus_interface='org.r2rk.
