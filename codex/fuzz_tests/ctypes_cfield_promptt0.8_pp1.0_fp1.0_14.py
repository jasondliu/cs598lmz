import ctypes
# Test ctypes.CField.from_address()
# http://docs.python.org/dev/library/ctypes.html#ctypes.CField.from_address

libc = ctypes.CDLL(ctypes.util.find_library("c"))

# This is due to a change in the itertools API in Python 3.2
try:
    izip = izip
except NameError:
    from itertools import zip_longest as izip

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

x = X(1, 2)
px = ctypes.pointer(x)
px2 = ctypes.c_void_p.from_address(ctypes.addressof(x))

if px != px2:
    raise Exception("from_address() failed")

# Changes to ctypes.Structure doesn't affect ctypes.c_void_p fields
# (Because they are stored as an integer)
x.b = 10
px.
