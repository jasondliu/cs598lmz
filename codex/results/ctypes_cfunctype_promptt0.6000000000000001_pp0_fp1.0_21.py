import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_void_p, ctypes.POINTER, ctypes.byref(),
# ctypes.cast()

# Test if ctypes can be used to call a C callback function from Python.
# The callback function is called from C, and returns a value.
# The callback function is passed a pointer to a structure.

import _ctypes_test

libc = ctypes.CDLL(ctypes.util.find_library("c"))

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char_p)]

Xp = ctypes.POINTER(X)

def callback(xp):
    return xp.contents.a * 2

CallbackType = ctypes.CFUNCTYPE(ctypes.c_int, Xp)

callback = CallbackType(callback)

libc.set_callback(callback)

x = X(_ctypes_test.get_x())

# call the C function which calls back into Python
result = lib
