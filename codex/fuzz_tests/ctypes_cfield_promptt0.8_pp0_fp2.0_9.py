import ctypes
# Test ctypes.CField class
try:
    class CFoo(ctypes.Structure):
        pass
    CFoo._fields_ = [("foo", ctypes.c_int)]
except TypeError:
    pass
# /Test ctypes.CField class

# Test ctypes.WINFUNCTYPE class
try:
    ctypes.WINFUNCTYPE(ctypes.c_int)
except TypeError:
    pass
# /Test ctypes.WINFUNCTYPE class

# Test ctypes.CFUNCTYPE class
try:
    ctypes.CFUNCTYPE(ctypes.c_int)
except TypeError:
    pass
# /Test ctypes.CFUNCTYPE class

# Test ctypes.POINTER class
try:
    ctypes.POINTER(ctypes.c_int)
except TypeError:
    pass
# /Test ctypes.POINTER class

# Test ctypes.Structure class
try:
    class Foo(ctypes.Structure):
        pass
    Foo._fields_ = [("foo", ctypes.c_int
