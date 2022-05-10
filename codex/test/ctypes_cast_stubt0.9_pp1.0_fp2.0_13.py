import ctypes
ctypes.cast(b'string', ctypes.POINTER(ctypes.c_ubyte))
class cls_example(ctypes.Structure):
    _fields_ = [('a', ctypes.c_ubyte), ('b', ctypes.c_ubyte)]
ctypes.cast(b'AB', ctypes.POINTER(cls_example))

# example 2
