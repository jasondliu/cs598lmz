import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double('3.14')

assert(str(S.x) == 'c_double(3.14)')
