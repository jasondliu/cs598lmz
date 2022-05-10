import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/tmp/example.db')

# This is copied from Wikipedia
#tutorials.tutorials:tutorials:tutorials

import dbus
import dbus.mainloop.glib
import dbus.service

try:
    from gi.repository import GObject
except ImportError:
    import gobject as GObject

LOGLEVEL_INFO = 0
LOGLEVEL_WARNING = 1
LOGLEVEL_ERROR = 2

class OcLogApi():
    
    log_level = 0
    
    sqllite_db_path = "/tmp/example.db"
    sqllite_table_name = "OcLogger"
    
    def __init__(self):
        self.log = OcLog()
        pass
    
    def info(self, msg):
        self.log.info(msg)
        return 0
    
    def warning(self, msg):
        self.log.warning(msg)
        return 0
    
    def error(self, msg):
        self.log.error(msg
