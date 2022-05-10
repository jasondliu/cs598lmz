import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16

# the following is the important part:
# in ctypes.c_int32, ctypes.c_int16 and ctypes.c_int8
# 'short' and 'int' are different!

assert ctypes.c_int16 is ctypes.c_int2
assert ctypes.c_int32 is ctypes.c_int4
assert ctypes.c_int64 is ctypes.c_int8
assert ctypes.c_int64.__name__ == 'c_int8'

assert ctypes.c_int16.__name__ == 'c_int16'

assert type(S.x) is ctypes.c_int16

assert ctypes.c_int is ctypes.c_long

assert ctypes.c_int32 is ctypes.c_int
assert ctypes.c_int64 is ctypes.c_longlong
assert ctypes.c_int16 is ctypes.c_short
assert ctypes.c_int8 is ctypes.c_byte

assert ctypes.c_
