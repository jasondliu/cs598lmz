import ctypes
import ctypes.util
import threading
import sqlite3
import time

# Global variables
db_path = '/tmp/pi-heating-hub/pi-heating-hub.db'
#db_path = '/Users/david/pi-heating-hub/pi-heating-hub.db'

# Commands

class command_t(ctypes.Structure):
    _fields_ = [("cmd_id", ctypes.c_int),
                ("zone", ctypes.c_int),
                ("setpoint", ctypes.c_double),
                ("duration", ctypes.c_long)]

class command_buffer_t(ctypes.Structure):
    _fields_ = [("lock", ctypes.c_int),
                ("size", ctypes.c_int),
                ("head", ctypes.c_int),
                ("tail", ctypes.c_int),
                ("cmds", command_t * 8)]


class PiHeatingHub(object):
    """A class to control a Raspberry Pi powered home heating system"""

