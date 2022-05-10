import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    print("func:", x)

cfunc = ctypes.CFUNCTYPE(None, ctypes.c_int)(func)
cfunc(42)

cfunc = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: print("lambda:", x))
cfunc(42)
import ctypes
# Test ctypes.cast

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X(42)
print(ctypes.cast(x, ctypes.c_void_p).value)
import ctypes
# Test ctypes.POINTER

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X(42)
p = ctypes.pointer(x)
print(p.contents.a)
import ctypes
# Test ctypes.byref

class X(ctypes.Structure):
    _fields_ = [("a",
