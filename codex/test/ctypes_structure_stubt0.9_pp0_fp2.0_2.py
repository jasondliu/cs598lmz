import ctypes

class S(ctypes.Structure):
    x = [ctypes.c_void_p] # TypeError: 'c_void_p' object cannot be interpreted as an index

r1 = id(S.x)
r2 = id(S.x[0]) # TypeError: 'c_void_p' object cannot be interpreted as an index
