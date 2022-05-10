import ctypes
# Test ctypes.CField
ctypes.sizeof(ctypes.CField()) == ctypes.sizeof(ctypes.c_void_p)

# Test ctypes.Structure
class X(ctypes.Structure):
    _fields_ = []
ctypes.sizeof(X())

# Test ctypes.Array
ctypes.sizeof(ctypes.Array(ctypes.c_int, 10))

# Test ctypes.Union
class Y(ctypes.Union):
    _fields_ = []
ctypes.sizeof(Y())

# Test ctypes.Union's attribute access
Y(p=Y())
