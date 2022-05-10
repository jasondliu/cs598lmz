import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import random
import string
import glob
import sys

# The following function is from the pycrypto package that
# can be found here: https://www.dlitz.net/software/pycrypto/
# License: Public Domain
#
# The following is not a copy of the original code. I have
# stripped out the parts that I do not need.
#
# This is not a perfect substitute for the real thing, but
# it is good enough for this application.
def _fastmath(libname):
    """
    Load the specified library and set the
    ctypes function argtypes.
    """
    lib = ctypes.CDLL(libname)
    lib.BN_mod_exp.argtypes = [ctypes.c_void_p, ctypes.c_void_p,
                               ctypes.c_void_p, ctypes.c_void_p,
                               ctypes.c_void_p, ctypes.c_void_p]
    return lib

try:
    _fastmath = _fastmath(ctypes.
