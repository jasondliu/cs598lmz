import ctypes
import ctypes.util
import threading
import sqlite3
import struct
import time

DEBUG = 0

COMM_FREQUENCY = 250000
COMM_WINDOW_SIZE = 64
COMM_TIMEOUT = 500

TELEMETRY_FREQUENCY = 5
TELEMETRY_WINDOW_SIZE = 64
TELEMETRY_TIMEOUT = 500

ERROR_SUCCESS = 0
ERROR_TIMEOUT = 0x110
ERROR_INVALID_DATA = 0x7e

class Parameter:
    def __init__(self, id, name, type, value=0):
        self.id = id
        self.name = name
        self.type = type
        self.value = value
        self.readonly = False

class GetParameter(Parameter):
    def __init__(self, id, name, type):
        Parameter.__init__(self, id, name, type)
        self.readonly = True

class SetParameter(Parameter):
    def __init__(self, id, name, type, value):
        Parameter.__init__(self, id, name
