import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import math
import string
import subprocess

from ctypes import c_int, c_double, c_float, c_char_p, POINTER, c_void_p, c_char
from ctypes import Structure

from utils import is_number, is_int, is_float_int, is_float, is_string
import constants
import logger
import functions
import config

lib = ctypes.CDLL(ctypes.util.find_library(constants.DBUS_LIB))

def dbus_shutdown():
    """
    Call dbus shutdown and then unload the shared library.
    """
    try:
        lib.dbus_shutdown()
    except e:
        print "Unable to shutdown dbus: ", e

class DBusError(Exception):
    """
    Exception to be thrown when there are problems with the dbus.
    """

    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

