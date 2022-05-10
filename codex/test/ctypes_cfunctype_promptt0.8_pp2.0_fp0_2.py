import ctypes
# Test ctypes.CFUNCTYPE, CFUNCTYPE(None, ctypes.c_int)
class X(ctypes.Structure):
    pass
x = ctypes.c_int()
X._fields_ = [('f0', ctypes.CFUNCTYPE(None, ctypes.c_int)),
              ('f1', ctypes.CFUNCTYPE(None, ctypes.c_int))]

