import ctypes
# Test ctypes.CFUNCTYPE
print(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    (lambda x,y: x)(1,2))
# Test ctypes.c_void_p
print(ctypes.c_void_p(1))
# Test ctypes.POINTER(ctypes.c_int)
class P:
    _type_ = ctypes.c_int
