import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# _ctypes.PyDLL is a subclass of ctypes.CDLL
_ctypes = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

# Set up the prototype and parameters of the C function to call.
_ctypes.strtol.restype = ctypes.c_long
_ctypes.strtol.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int)

# Convert the Python string to a ctypes char array and call the C function.
def strtol(s, base=0):
    c_s = ctypes.c_char_p(s)
    endptr = ctypes.c_char_p()
    result = _ctypes.strtol(c_s, ctypes.byref(endptr), base)
    if endptr.value:
        return result, endptr.value - c_s.value
    else:
        return
