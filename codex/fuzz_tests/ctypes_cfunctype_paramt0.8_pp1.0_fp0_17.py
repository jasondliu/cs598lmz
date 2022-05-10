import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

cfunc = FUNTYPE(lambda x: x + 1)
assert cfunc(2) == 3

def func(x):
    return 2 * x

assert func(3) == 6

cfunc = FUNTYPE(func)
assert cfunc(2) == 4

# (There is a bug involving conversion of Python functions
#  with a closure to ctypes callback functions.)

#------------------------------------------------------------------------------
# Shim functions

# ctypes automatically converts ctypes arguments to types that
# the C function expects.

from ctypes import c_char_p
strlen = cdll.msvcrt.strlen
assert strlen(c_char_p("Hello world")) == 11

# ctypes converts Python unicode strings to C strings,
# i.e. bytes.

assert strlen(u"Hello world") == 11

strlen.restype = ctypes.c_size_t
assert strlen(u"Hello world") == 11

#------------------------------------------------------------------------------
# Pointers

from ctypes import c_int
