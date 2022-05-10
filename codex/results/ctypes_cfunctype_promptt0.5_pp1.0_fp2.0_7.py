import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(arg):
    print arg

CFUNCTYPE(c_int, c_int)(func)(42)

# Test ctypes.POINTER(c_int)

p = POINTER(c_int)()
assert p.contents is None
p = POINTER(c_int)(c_int(42))
assert p.contents.value == 42

# Test ctypes.c_buffer

class X(Union):
    _fields_ = [("a", c_int),
                ("b", c_char * 4)]

x = X()
x.a = 42
assert x.b == "*" * 4
x.b = "spam"
assert x.a == 0x737061

# Test ctypes.c_char_p

x = c_char_p("spam")
assert x.value == "spam"
assert x.value == x.raw
assert x.value == x[:]

# Test ctypes.c_wchar_p

x = c_
