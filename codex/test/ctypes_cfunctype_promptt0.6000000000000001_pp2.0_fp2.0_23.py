import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
def cb(s):
    return len(s)

class C(ctypes.Structure):
    _fields_ = [('cb', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p))]

