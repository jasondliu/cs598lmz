import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with timeout values.

SetConfig = None
GetConfig = None
ConfigOption = None
Thread = None

dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

def setUpModule():
    global SetConfig, ConfigOption, GetConfig
    global Thread

    if sys.version_info >= (3,):
        unicode = str
        SetConfig = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                ctypes.c_int)(("sqlite3_test_control", dll), ((1, "op"), (1, "value")))
    else:
        SetConfig = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                ctypes.c_int)(("sqlite3_test_control", dll), ((1, "op", 0), (1, "value")))

    GetConfig = ctypes.CFUNCTYPE(ctypes.c_uint)(("sqlite3_test_control", dll),
            ((1
