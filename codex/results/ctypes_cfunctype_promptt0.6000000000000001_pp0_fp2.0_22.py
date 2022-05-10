import ctypes
# Test ctypes.CFUNCTYPE.

import _ctypes_test

lib = ctypes.cdll.LoadLibrary(_ctypes_test.__file__)

#char func(char, char)
f = lib.func
f.argtypes = ctypes.c_char, ctypes.c_char
f.restype = ctypes.c_char

print(f(b'a', b'b'))

# void func(char, char)
f = lib.func
f.argtypes = ctypes.c_char, ctypes.c_char
f.restype = None

f(b'z', b'x')

# void func(char, char)
f = lib.func
f.argtypes = ctypes.c_char, ctypes.c_char
f.restype = ctypes.c_byte

f(b'z', b'x')
