import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint()
    y = ctypes.c_uint()

class R(ctypes.Structure):
    _fields_ = [("x",ctypes.c_uint),("y",ctypes.c_uint)]
