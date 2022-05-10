import ctypes
# Test ctypes.CFUNCTYPE.
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

def callback(x):
    x.a = 7

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.printf()
CALLBACK = ctypes.CFUNCTYPE(None, ctypes.POINTER(X))
p = ctypes.pointer(X(42))
libc.qsort(p, 1, ctypes.sizeof(X), CALLBACK(callback))
print(p[0].a)
