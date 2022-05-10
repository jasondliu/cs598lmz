import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p)
arch = platform.machine()
libc = cdll.msvcrt if arch.startswith('AMD64') else cdll.LoadLibrary("libc.so.6")
libc.rand = libc.rand_s
print libc.rand(0, 0)
