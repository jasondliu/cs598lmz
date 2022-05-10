import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print("a=%d, b=%d" % (a, b))
    return a + b

f = FUNTYPE(myfunc)

f(1, 2)

# 如果要把一个Python函数转换成一个C函数，需要一个指针，可以使用ctypes.cast()函数：

# >>> from ctypes import *
# >>> libc = CDLL("libc.so.6")
# >>> libc.printf("Hello, World!\n")
# Hello, World!
# 13
# >>> libc.printf.argtypes = [c_char_p]
# >>> libc.printf("Hello, World!\n")
# Hello, World!
# 13
# >>> libc.printf("Hello, %s
