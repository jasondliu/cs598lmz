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

