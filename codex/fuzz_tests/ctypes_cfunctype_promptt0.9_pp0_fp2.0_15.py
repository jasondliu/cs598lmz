import ctypes
# Test ctypes.CFUNCTYPE
int_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
int_func(3)

# Test ctypes.c_int
# PyPy uses <cffi type, PyPy value>; cpython is <cffi type, ctypes object>
c_int_good = ctypes.c_int(3)
c_byte_good = ctypes.c_byte(3)

# All the ctypes.XXX types are convertible; ctypes.c_byte is convertible from bytestring.
c_int_not_good = ctypes.c_int(3.1416)
c_byte_not_good = ctypes.c_byte(3.1416)
