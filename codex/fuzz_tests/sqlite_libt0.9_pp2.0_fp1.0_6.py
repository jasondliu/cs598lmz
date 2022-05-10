import ctypes
import ctypes.util
import threading
import sqlite3
import json
import time

# struct LnkInfo {
#     int32  magic;
#     int32  code;
#     int32  size;
# }
class LnkInfo(ctypes.Structure):
    _fields_ = [("magic", ctypes.c_int),
                ("code", ctypes.c_int),
                ("size", ctypes.c_int),
               ]
    _pack_ = 1

# struct WbItem {
#     int32  size;
#     int32  type;
#     int32  tabid;
#     char   url[256];
#     char   title[256];
# }
class WbItem(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int),
                ("type", ctypes.c_int),
                ("tabid", ctypes.c_int),
                ("url", ctypes.c_char * 256),
                ("title", ctypes.c_char * 256),
               ]
    _pack_ = 1

#
