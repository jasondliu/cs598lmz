import ctypes
# Test ctypes.CField structure
class S(ctypes.Union):
    _fields_ = [('f1', ctypes.c_char), ('f2', ctypes.c_int), ('f3', ctypes.c_char_p)]
print(S.f1)
print(S.f2)
print(S.f3)
# Test CField.offset attribute
class S1(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char), ('b', ctypes.c_int)]
print(S1.a.offset)
print(S1.b.offset)
# Test ctypes.Field structure
class S2(ctypes.Structure):
    _fields_ = [('f1', ctypes.c_char), ('f2', ctypes.c_int), ('f3', ctypes.c_char_p)]
print(S2.f1)
print(S2.f2)
print(S2.f3)
# Test CField.offset attribute
class S3(ctypes.Structure):
    _fields_ = [
