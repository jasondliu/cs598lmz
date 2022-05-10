import ctypes
# Test ctypes.CField, ctypes.Field
class S2(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_short)]

s = S2(3, 4)
assert ctypes.CField(S2).from_address(ctypes.addressof(s)).value == 3
assert ctypes.CField(S2.a).from_address(ctypes.addressof(s)).value == 3
assert ctypes.Field(S2.a).from_address(ctypes.addressof(s)).value == 3
assert ctypes.Field(S2.b).from_address(ctypes.addressof(s) + ctypes.sizeof(ctypes.c_int)).value == 4

# Test ctypes.POINTER_T, ctypes.POINTER(type)
class S3(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_short)]

assert ctypes.POINTER(S3) == ctypes.POINTER
