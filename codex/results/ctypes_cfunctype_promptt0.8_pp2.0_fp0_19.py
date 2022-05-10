import ctypes
# Test ctypes.CFUNCTYPE
class C(object):
    pass
C._fields_ = [('a', ctypes.c_int)]
test_cfunctype_class = C
C_p = ctypes.POINTER(C)
argtypes = (C_p, C_p)
CFUNCTYPE_CLASS_TEST_1 = ctypes.CFUNCTYPE(ctypes.c_int, *argtypes)(CFUNCTYPE_CLASS_TEST_1)
result = CFUNCTYPE_CLASS_TEST_1(ctypes.POINTER(C)(1), ctypes.POINTER(C)(2))
