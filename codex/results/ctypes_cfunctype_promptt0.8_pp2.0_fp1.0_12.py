import ctypes
# Test ctypes.CFUNCTYPE
libc = cdll.LoadLibrary("libc.so.6")
printf = libc.printf
printf.restype = ctypes.c_int
printf.argtypes = [ctypes.c_char_p]
printf("Hello, World\n")
</code>

