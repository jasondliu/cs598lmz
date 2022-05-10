import ctypes
import ctypes.util
import threading
import sqlite3
import os.path

# TODO:
# - Use the local timezone
# - Add a way to remove a user from the database
# - Add a way to remove a user from the database
# - Add a way to remove a user from the database

class AmbientLightSensor(object):
    def __init__(self, device, channel, grp):
        self.device = device
        self.channel = channel
        self.grp = grp
        self.fd = None

    def open(self):
        if self.fd:
            return True
        self.fd = os.open(self.device, os.O_RDONLY)
        if not self.fd:
            return False
        return True

    def close(self):
        if not self.fd:
            return True
        os.close(self.fd)
        self.fd = None
        return True

    def poll(self):
        if not self.open():
            return None
        buf = array.array('H', [0, 0, 0, 0])
        res = fcnt
