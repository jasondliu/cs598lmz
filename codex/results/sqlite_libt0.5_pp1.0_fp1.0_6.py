import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time

import pdb

class Fuse(ctypes.Structure):
    _fields_ = [
        ("fh", ctypes.c_ulong),
        ("open_flags", ctypes.c_int),
        ("padding", ctypes.c_int * 117),
    ]

class DirBuf(ctypes.Structure):
    _fields_ = [
        ("size", ctypes.c_int),
        ("used", ctypes.c_int),
        ("error", ctypes.c_int),
        ("buf", ctypes.c_char_p),
        ("filler", ctypes.c_void_p),
    ]

class FileInfo(ctypes.Structure):
    _fields_ = [
        ("flags", ctypes.c_int),
        ("fh_old", ctypes.c_ulong),
        ("writepage", ctypes.c_int),
        ("direct_io", ctypes.c_uint, 1),
        ("keep_cache", ctypes.c_
