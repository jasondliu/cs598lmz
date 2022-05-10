import ctypes
# Test ctypes.CFUNCTYPE(...)(...), ctypes.c_char_p(...), libc.printf
libc = ctypes.cdll.LoadLibrary("libc.so.6")

c_printf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(("printf", libc))
