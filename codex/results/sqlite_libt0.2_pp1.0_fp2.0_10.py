import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys

# TODO:
# - add support for more than one device
# - add support for more than one database

# TODO:
# - add support for more than one device
# - add support for more than one database

class Device(object):
    def __init__(self, path):
        self.path = path
        self.lib = ctypes.CDLL(ctypes.util.find_library('hidapi'))
        self.lib.hid_init()
        self.handle = self.lib.hid_open_path(path)
        self.buffer = ctypes.create_string_buffer(8)
        self.buffer[0] = 0x01
        self.buffer[1] = 0x80
        self.buffer[2] = 0x33
        self.buffer[3] = 0x01
        self.buffer[4] = 0x00
        self.buffer[5] = 0x00
        self.buffer[6] = 0x00
        self.buffer[7] = 0x00
        self
