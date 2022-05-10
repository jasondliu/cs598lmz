import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2
print(s.x, s.y)

# ctypes.c_int -> ctypes.c_int32
# ctypes.c_float -> ctypes.c_float32

# ctypes.c_int -> ctypes.c_int64
# ctypes.c_float -> ctypes.c_float64

# ctypes.c_int -> ctypes.c_int16
# ctypes.c_float -> ctypes.c_float16

# ctypes.c_int -> ctypes.c_int8
# ctypes.c_float -> ctypes.c_float8

# ctypes.c_int -> ctypes.c_int128
# ctypes.c_float -> ctypes.c_float128

# ctypes.c_int -> ctypes.c_int256
# ctypes.c_float -> ctypes.c_float256

# ctypes.c_int -> ctypes
