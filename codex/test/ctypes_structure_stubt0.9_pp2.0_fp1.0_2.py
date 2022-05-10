import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16() # also fails if set to c_int
class N(ctypes.Structure):
    _fields_ = [('nested', S)]

x = N()
