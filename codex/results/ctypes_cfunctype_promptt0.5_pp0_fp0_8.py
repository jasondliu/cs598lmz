import ctypes
# Test ctypes.CFUNCTYPE with non-void return type

# This is a "return int" test
libc = CDLL(ctypes.util.find_library("c"))

# XXX This test is not working yet...

# int putchar(int c);
putchar = libc.putchar
putchar.argtypes = (c_int,)
putchar.restype = c_int

# int (*)(int)
putchar_p = CFUNCTYPE(c_int, c_int)(putchar)

print putchar_p(ord("t"))
print putchar_p(ord("e"))
print putchar_p(ord("s"))
print putchar_p(ord("t"))
print putchar_p(ord("\n"))

# int putchar2(int c);
putchar2 = libc.putchar
putchar2.argtypes = (c_int,)
putchar2.restype = c_int

# int (*)(int)
putchar2_p = CFUNCTYPE(c_int, c_int)(putchar2)


