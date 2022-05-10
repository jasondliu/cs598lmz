import ctypes
import ctypes.util
import threading
import sqlite3
import time

from ctypes import CDLL, POINTER, Structure, byref, c_char_p, c_void_p, c_int, c_uint, c_float, c_double, c_ulonglong, c_longlong, c_size_t, c_bool
from ctypes import py_object as c_object
from ctypes.wintypes import MSG, HWND, LPARAM, UINT, LPVOID, BOOL, WPARAM, DWORD, LONG, HANDLE
import numpy as np

import pygame

from pygame.locals import *

import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)


class Vector3(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
    ]

class RigidBody(Structure):
    _fields_ = [
        ('name', c_char_p),
        ('id', c_int),
        ('parent
