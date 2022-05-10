import ctypes
import ctypes.util
import threading
import sqlite3

from PyQt5.QtCore import QObject, pyqtSignal

from . import utils

class DBusObject(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dbus_path = None
        self.dbus_interface = None
        self.dbus_service = None
        self.dbus_bus = None
        self.dbus_object = None
        self.dbus_loop = None
        self.dbus_thread = None
        self.dbus_loop_thread = None
        self.dbus_loop_running = False
        self.dbus_loop_stop = False
        self.dbus_loop_stop_event = threading.Event()
        self.dbus_loop_stop_event.clear()
        self.dbus_loop_stop_event.set()
        self.dbus_loop_stop_event.clear()
        self.dbus_loop_stop_event.set()
        self.dbus_loop_stop_event
