import ctypes
# Test ctypes.CFUNCTYPE
print(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    (lambda x,y: x)(1,2))
# Test ctypes.c_void_p
print(ctypes.c_void_p(1))
# Test ctypes.POINTER(ctypes.c_int)
class P:
    _type_ = ctypes.c_int
print(ctypes.POINTER(P))
# Test ctypes.addressof
class P:
    _type_ = ctypes.c_int
p = ctypes.POINTER(P)()
print(ctypes.addressof(p))
# Test ctypes.cast
class P:
    _type_ = ctypes.c_int
p = ctypes.POINTER(P)()
print(p)
print(ctypes.cast(ctypes.addressof(p), ctypes.POINTER(ctypes.c_int)))
# Test ctypes.py_object
print(type(ctypes.py_object(
