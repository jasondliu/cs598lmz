import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

# int foo(int, int)
foo_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# int bar(int, int)
bar_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# int foo_bar(foo_t, bar_t)
foo_bar_c = ctypes.CFUNCTYPE(ctypes.c_int, foo_c, bar_c)

def foo(a, b):
    return a + b

def bar(a, b):
    return a - b

def foo_bar(a, b):
    return a(1, 2) + b(3, 4)

