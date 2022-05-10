import ctypes
# Test ctypes.CFUNCTYPE
def func(x):
    return x + 1

CFUNCTYPE(c_int)(func)(1)

# Test ctypes.POINTER
POINTER(c_int)

# Test ctypes.c_bool
c_bool(True)

# Test ctypes.c_wchar
c_wchar('a')

# Test ctypes.c_wchar_p
c_wchar_p('hello world')

# Test ctypes.c_char_p
c_char_p(b'hello world')

# Test ctypes.c_void_p
c_void_p(None)

# Test ctypes.c_char
c_char('a')

# Test ctypes.c_ubyte
c_ubyte(1)

# Test ctypes.c_byte
c_byte(1)

# Test ctypes.c_short
c_short(1)

# Test ctypes.c_ushort
c_ushort(1)

# Test ctypes.c_int
c_int
