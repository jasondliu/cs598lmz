import ctypes
import ctypes.util
import threading
import sqlite3 as sqlite
import scrypt
import base64
import getpass
import os

PASSWORD = "toto"

class EncodedFileHeader(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("start", ctypes.c_char * 8),
        ("id", ctypes.c_uint32),
        ("salt_len", ctypes.c_uint16),
        ("salt", ctypes.c_char * 64),
        ("iv_len", ctypes.c_uint16),
        ("iv", ctypes.c_char * 32),
        ("tag_len", ctypes.c_uint16),
        ("tag", ctypes.c_char * 16),
        ("file_len", ctypes.c_uint64)
    ]

    _paddings_ = {
        "start": 8,
        "salt": 64,
        "iv": 32,
        "tag": 16
    }

