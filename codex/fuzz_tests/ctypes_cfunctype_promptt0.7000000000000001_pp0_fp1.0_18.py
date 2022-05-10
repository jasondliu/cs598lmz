import ctypes
# Test ctypes.CFUNCTYPE(...)

# Testing a function pointer specified as an argument to another function:
# PyObject_CallFunction(..., CFUNCTYPE(...), ...)
#
# Testing a function pointer specified as a return value:
# CFUNCTYPE(...)(<function>)

# Enum values are passed to lib.SDL_EventType:
SDL_FIRSTEVENT = 0
SDL_MOUSEMOTION = 1
SDL_MOUSEBUTTONDOWN = 2

# CFUNCTYPE(<type>, <arguments>):
print "*** Testing CFUNCTYPE(<type>, <arguments>)..."
print "  - Normal function pointer as an argument"

c_callback = ctypes.CFUNCTYPE(
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_int))
def pyfunc(p):
    #print p[0]
    return p[0]*2

p_pyfunc = c_callback(pyfunc)

testlib = ctypes.CDLL(util.find_library
