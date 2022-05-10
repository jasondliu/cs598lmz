import ctypes
import ctypes.util
import threading
import sqlite3
import base64
import json
import sys
import os

from . import utils

class http_response_t(ctypes.Structure):
    _fields_ = [
        ("code", ctypes.c_char_p),
        ("header", ctypes.c_char_p),
        ("body", ctypes.c_char_p),
    ]

class vx_resolver_t(ctypes.Structure):
    _fields_ = [
        ("data", ctypes.c_char_p),
        ("size", ctypes.c_int),
        ("mime", ctypes.c_char_p),
    ]

class vx_request_t(ctypes.Structure):
    _fields_ = [
        ("path", ctypes.c_char_p),
        ("resolver", ctypes.POINTER(vx_resolver_t)),
        ("header", ctypes.c_char_p),
        ("body", ctypes.c_char_p),
    ]

class vx_response_t(ctypes
