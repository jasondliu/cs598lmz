import ctypes
# Test ctypes.CField
class A:
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_longlong),
                ("z", ctypes.c_ubyte)]

class B(A):
    _fields_ = [("a", ctypes.c_int)]

class C(A):
    _fields_ = [("b", ctypes.c_longlong)]

class D(B):
    _fields_ = [("c", ctypes.c_ubyte)]

class E(C, D):
    _fields_ = [("d", ctypes.c_short),
                ("e", ctypes.c_int),
                ("f", ctypes.c_longlong),
                ("g", ctypes.c_ubyte)]

class F(E):
    _fields_ = [("h", ctypes.c_int)]

F._fields_ = [("i", ctypes.c_int)]

# todo: _pack_ is not implemented yet

# The following classes were used for debugging
class S
