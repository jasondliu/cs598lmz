import ctypes
# Test ctypes.CFUNCTYPE
print(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))
# Test ctypes.POINTER
print(ctypes.POINTER(ctypes.c_int))
# Test ctypes.cast
print(ctypes.cast(42, ctypes.c_int))
# Test ctypes.c_byte
print(ctypes.c_byte(42))
# Test ctypes.c_char
print(ctypes.c_char(b'A'))
# Test ctypes.c_char_p
print(ctypes.c_char_p(b'ABC'))
# Test ctypes.c_double
print(ctypes.c_double(42.0))
# Test ctypes.c_float
print(ctypes.c_float(42.0))
# Test ctypes.c_int
print(ctypes.c_int(42))
# Test ctypes.c_int16
print(ctypes.c_int16(42))
# Test ctypes.c_int32
print(ctypes.c_
