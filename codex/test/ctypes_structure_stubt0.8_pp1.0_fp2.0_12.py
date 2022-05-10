import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32(1)
    def __repr__(self):
        return '<S>'

p = ctypes.POINTER(S)()
