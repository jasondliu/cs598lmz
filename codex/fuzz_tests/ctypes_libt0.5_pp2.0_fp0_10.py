import ctypes
ctypes.CDLL("libc.so.6")

from ctypes import *
libc = ctypes.CDLL("libc.so.6")

libc.puts("Hello, World!\n")
libc.printf("Hello, %s!\n", "World")
libc.printf("%d + %d = %d\n", 1, 2, 3)

libc.printf("%f\n", c_double(1.0))
libc.printf("%f\n", c_float(1.0))

libc.printf("%d\n", c_int(1))
libc.printf("%d\n", c_uint(1))
libc.printf("%d\n", c_long(1))
libc.printf("%d\n", c_ulong(1))
libc.printf("%d\n", c_longlong(1))
libc.printf("%d\n", c_ulonglong(1))

libc.printf("%d\n", c_short(1))
lib
