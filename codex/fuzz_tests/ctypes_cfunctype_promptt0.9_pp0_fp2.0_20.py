import ctypes
# Test ctypes.CFUNCTYPE versus strncpy
import sys
if sys.platform == "win32":
    libc = ctypes.CDLL('msvcrt')
elif sys.platform == "darwin":
    libc = ctypes.CDLL('libc.dylib')
else:
    libc = ctypes.CDLL('libc.so.6')

# strncpy
libc.strncpy.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t)
C_strncpy = libc.strncpy
C_strncpy.restype = ctypes.c_char_p

c_source = ctypes.create_string_buffer('0123456789abcdef', 16)
c_dest = ctypes.create_string_buffer(16)
C_strncpy(c_dest, c_source, 3)
print c_dest.raw, repr(c_dest.raw)

if sys.platform != "win32":
    C_strncpy(c_dest, c
