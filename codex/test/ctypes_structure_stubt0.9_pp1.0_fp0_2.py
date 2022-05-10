import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(ctypes.c_double)

class OtherStruct(ctypes.Structure):
    x = ctypes.c_char

def callback(s):
    s.test = ctypes.c_char('x')
