import ctypes
import ctypes.util
import threading
import sqlite3
import json
import os

from utils import data_file_path, c_str
from . import settings

OPENSSL_HANDLE = None

class TLSSession(ctypes.Structure):
    _fields_ = [
        ("device_id", ctypes.c_uint32),
        ("sess", ctypes.c_void_p),
        ("ssl", ctypes.c_void_p),
        ("ctx", ctypes.c_void_p),
        ("trusted", ctypes.c_bool),
        ("in_use", ctypes.c_void_p),
        ("bio", ctypes.c_void_p),
    ]

TLSSessionPtr = ctypes.POINTER(TLSSession)

"""Holds any pending incoming data that has not yet been read by the user."""
cbuffer = bytearray()

def _recv_callback(session, buf, length, userdata):
    import select
    global cbuffer

    if len(cbuffer) >= length:
        buf = ctypes.cast(
