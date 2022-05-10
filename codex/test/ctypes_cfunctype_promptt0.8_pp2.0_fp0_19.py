import ctypes
# Test ctypes.CFUNCTYPE
class C(object):
    pass
C._fields_ = [('a', ctypes.c_int)]
test_cfunctype_class = C
