import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import json
import logging
import logging.handlers

#
# This is the main class for the DLL
#
class DLL:
    def __init__(self, name):
        self.lib = ctypes.cdll.LoadLibrary(name)
        self.lib.init.restype = ctypes.c_int
        self.lib.init.argtypes = [ctypes.c_char_p]
        self.lib.get_data.restype = ctypes.c_char_p
        self.lib.get_data.argtypes = [ctypes.c_char_p]
        self.lib.get_data_json.restype = ctypes.c_char_p
        self.lib.get_data_json.argtypes = [ctypes.c_char_p]
        self.lib.get_data_json_async.restype = ctypes.c_char_p
        self.lib.get_data_json_async.argtypes = [ctypes.c_char_p]

