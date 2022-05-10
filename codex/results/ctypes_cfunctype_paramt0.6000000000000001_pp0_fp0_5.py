import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@FUNTYPE
def f(x, y):
    return x+y

f(1, 2)

# but if the return type is not specified, it is a python function type and
# can not be passed to a function expecting a function pointer.

@ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
def g(x, y):
    return x+y

# but we can use the actual function type to create a new wrapper that
# can be used

def h(x, y):
    return x+y

h_wrapper = FUNTYPE(h)
h_wrapper(1,2)

# but the wrapper is not a ctypes function type, so it can not be passed
# to a function expecting a function pointer.

# but we can use the actual function type to create a new wrapper that
# can be used

def h(x, y):
    return x+y

h_wrapper = FUNTYPE
