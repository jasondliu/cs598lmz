import ctypes
# Test ctypes.CFUNCTYPE()
# Example from ctypes documentation: https://docs.python.org/3.3/library/ctypes.html?highlight=ctypes#ctypes._FuncPtr

import ctypes

libc = ctypes.CDLL(None)

c_uint8 = ctypes.c_uint8
c_voidp = ctypes.c_void_p

c_uint8_p = ctypes.POINTER(c_uint8)

memset = libc.memset
memset.argtypes = (c_voidp, c_uint8, ctypes.c_size_t)

data = bytearray(b'\xaa' * 1024)

buffer = (c_uint8 * len(data)).from_buffer(data)

memset(buffer, 0, len(data))
buffer

# memset.argtypes = (None, ctypes.c_uint8, ctypes.c_size_t)
# memset(c_voidp(buffer), c_uint8(0), ctypes.c_size_t(len(
