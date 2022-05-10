import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)


def cb(a, b):
    print "%d + %d = %d" % (a, b, a + b)
    return 0


f = FUNTYPE(cb)
test(f)
</code>

My assumption would be that multiple threads are not possible when using SWIG, but I wanted to double check.
If this is true, what is the best way to go about binding a C library that uses global variables and functions (for function pointers) to Python?

