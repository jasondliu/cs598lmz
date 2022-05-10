import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a+b

f = ctypes.CFUNCTYPE(ctypes.c_int)(func)

print f(1, 2)

# Test ctypes.c_void_p
import ctypes

x = ctypes.c_void_p(123)
print x.value

# Test ctypes.c_char_p
import ctypes

x = ctypes.c_char_p("Hello")
print x.value

# Test ctypes.c_char
import ctypes

x = ctypes.c_char('H')
print x.value

# Test ctypes.c_int
import ctypes

x = ctypes.c_int(123)
print x.value

# Test ctypes.c_short
import ctypes

x = ctypes.c_short(123)
print x.value

# Test ctypes.c_long
import ctypes

x = ctypes.c_long(123)
print x.value

# Test
