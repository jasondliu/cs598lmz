import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import logging
import subprocess
import re
import struct
import binascii

if sys.version_info[0] == 2:
    import Queue as queue
else:
    import queue as queue

# This is a hack to get around the fact that the library name is different
# on some platforms.
# TODO: Find a better way to do this.
for libname in ['libsodium', 'sodium']:
    try:
        sodium = ctypes.cdll.LoadLibrary(ctypes.util.find_library(libname))
        break
    except OSError:
        pass

# This is some magic to figure out the size of the sodium_secretbox_KEYBYTES
# constant.
assert sodium.sodium_init() == 0
sodium.sodium_bin2hex.restype = ctypes.c_char_p
sodium.sodium_bin2hex.argtypes = [ctypes.c_char_p, ctypes.c_size_t,
                                  ctypes.c_char
