import ctypes
import ctypes.util
import threading
import sqlite3

from .util import clean, args, insert_db

### util functions ###

try:
    _libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))
    _libc.setenv.restype = ctypes.c_int
    _libc.setenv.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]

    def setenv(name, value, overwrite=True, r_bouncer=True):
        _libc.setenv(name, value, overwrite)

    def find_cmd(name, path=None):
        if path is None:
            # This reliably gets the path with globs expanded and non-existent
            # directories filtered.
            path = os.getenv("PATH").split(os.path.pathsep)

        for dir in path:
            if not dir:
                continue
            cmd = os.path.join(dir, name)
            if os.path.exists(cmd):
                return cmd

    def x
