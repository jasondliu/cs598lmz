import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_char_p)
def bb(s):
    return s == b'q'

# Test ctypes.CFUNCTYPE with non-primitive return type
class X(ctypes.Structure):
    pass
X._fields_ = [
    ('a', ctypes.c_int)
]

