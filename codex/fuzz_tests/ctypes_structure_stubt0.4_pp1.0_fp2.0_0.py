import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [("x", ctypes.c_int)]

class D(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [("x", ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    x = ctypes.c_int()

class G(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    x = ctypes.c_int()

class H(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    x = ctypes.c_int()
    _fields_ = [("x", ctypes.c_int)]

class I(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
   
