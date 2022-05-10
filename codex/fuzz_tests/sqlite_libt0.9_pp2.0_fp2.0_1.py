import ctypes
import ctypes.util
import threading
import sqlite3
import queue
import time

def print_error(*args):
    print('DEBUG: ', end='')
    print(*args)

# libc.so
imessage = None

# libimessaged.dylib
imessaged = None

_idle_lock = threading.Lock()
_idle_proc = None
_idle_thread = None
_idle_finish_cvar = threading.Condition()

_service_does_not_exist = """\
service_callback: service '{}' does not exist
This is likely because the device_name which is currently set in the
libimessaged.dylib preferences is wrong.
"""

def start():
    global imessage
    global imessaged
    # load the libimessage.dylib library
    if 'i386' in platform.machine():
        imessage = ctypes.CDLL('libimessage.dylib')
        imessaged = ctypes.CDLL('libimessaged.dylib')
    else:
        path = ctypes.util.find_library('imessaged')

