import ctypes
# Test ctypes.CFUNCTYPE
libc = ctypes.CDLL(None)
func = libc.printf
func.argtypes = ctypes.c_char_p,
func.restype = ctypes.c_int
func(b"Hello, %s!\n", b"World")
# Test ctypes.POINTER
libc.printf(b"Hello, %s!\n", b"World")
# Test ctypes.c_bool
libc.printf(b"%i\n", ctypes.c_bool(True))
# Test ctypes.c_byte
libc.printf(b"%i\n", ctypes.c_byte(1))
# Test ctypes.c_char
libc.printf(b"%c\n", ctypes.c_char(b"A"))
# Test ctypes.c_char_p
libc.printf(b"%s\n", ctypes.c_char_p(b"A"))
# Test ctypes.c_double
libc.printf(b"%f\n", ctypes.c_double(1.0
