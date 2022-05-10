import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os

from win32com.shell import shell, shellcon
import win32con

from .. import interfaces

from .. import util

_libc_path = ctypes.util.find_library('c')
_libc = ctypes.CDLL(_libc_path, use_errno=True)

_libc.getpgrp.restype = ctypes.c_int
_libc.getpid.restype = ctypes.c_int

_libc_path = ctypes.util.find_library('pthread')
_libpthread = ctypes.CDLL(_libc_path, use_errno=True)

_libpthread.pthread_mutex_init.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
_libpthread.pthread_mutex_init.restype = ctypes.c_int
_libpthread.pthread_mutex_lock.argtypes = [ctypes.c_void_p]
_libpthread.pthread_
