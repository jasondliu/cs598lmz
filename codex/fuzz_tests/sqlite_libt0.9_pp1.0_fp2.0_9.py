import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
c_millisecond = ctypes.c_uint32
c_bool = ctypes.c_int
POSIX = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

class record(ctypes.Structure):
    """
    struct record {
        int id;
	long pos;
	unsigned long millisecond;
	int is_movie;
	int is_splay;
	int option;
	int length;
	int temporary;
	int mode;
    };
    """
    _fields_ = [("id", ctypes.c_int),
                ("pos", ctypes.c_int),
                ("millisecond", c_millisecond),
                ("is_movie", c_bool),
                ("is_splay", c_bool),
                ("option", c_bool),
                ("length", ctypes.c_int),
                ("temporary", ctypes.c_int),
                ("mode", ctypes.c_int)]


class FILE(ctypes
