import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

# declare a wrapper for the C-function that takes a Python function as an argument
# and returns a C-function pointer
@library.register
def _register_wrap(lib, f):
    c_f = FUNTYPE(f)
    lib.wrap.argtypes = [FUNTYPE]
    lib.wrap.restype = FUNTYPE
    return lib.wrap(c_f)

# use the wrapper to wrap a Python function and call it
@library.register
def _register_call(lib, f):
    lib.call.argtypes = [FUNTYPE]
    lib.call.restype = ctypes.c_double
    return lib.call(f)

# define the actual Python function that we want to call from C
@library.register
def _register_func(lib):
    def f(x, y):
        return x * y
    return f


# create a C wrapper for the Python function
f_c = wrap(func)

# call the C wrapper
print
