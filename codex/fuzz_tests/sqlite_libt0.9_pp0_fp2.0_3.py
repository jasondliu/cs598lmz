import ctypes
import ctypes.util
import threading
import sqlite3
import hashlib
import struct
import sys

# Hack because PyInstaller makes us use dlls instead of the normal on disk version
g_dirpath = os.path.dirname(os.path.realpath(__file__))
libsystem_c = ctypes.cdll.LoadLibrary(os.path.join(g_dirpath, "..", "..", "libsystemc.dylib"))

GSMC_SYMBOL = '_gsmc_find_symbol'
CALL_INT_SIG = 'i(ip)p'
CALL_VOID_SIG = 'v(ip)p'
CALL_BOOL_SIG = 'i(ip)p'
CALL_FLOAT_SIG = 'd(ip)p'
CALL_STRING_SIG = 's(ip)p'
gsmc_find_symbol = libsystem_c.gsmc_find_symbol
gsmc_find_symbol.argtypes = [ctypes.c_void_p]
gsmc_find_symbol.
