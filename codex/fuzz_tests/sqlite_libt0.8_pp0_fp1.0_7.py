import ctypes
import ctypes.util
import threading
import sqlite3
import os

import dbus.service
import dbus.glib

import log

from datetime import datetime

class Obexd(dbus.service.Object):
    """
    An Obexd client
    """

    def __init__(self, path, bus_name, object_path='/'):
        dbus.service.Object.__init__(self, bus_name, object_path)
        self.__bus_name = bus_name
        self.__path = path
        self.__db = sqlite3.connect(os.path.join(path, "obexd.db"))
        self.__mutex = threading.RLock()

        log.info("= OBEXD CLIENT =")
        log.info("Path: %s" % (path))

    def __del__(self):
        self.__db.close()

    def __get_transfer_id(self):
        cursor = self.__db.cursor()
        cursor.execute('SELECT id FROM transfer ORDER BY id DESC LIMIT 1')
        max
