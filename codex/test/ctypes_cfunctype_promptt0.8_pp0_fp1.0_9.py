import ctypes
# Test ctypes.CFUNCTYPE.

# Make sure this compiles.
class obj(ctypes.Structure):
    _fields_ = [("val", ctypes.c_int)]
o = obj()
callback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)(lambda x: None)
callback(ctypes.pointer(o))
