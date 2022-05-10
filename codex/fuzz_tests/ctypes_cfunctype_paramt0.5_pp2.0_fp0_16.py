import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_wrapper(name):
    func = getattr(c, name)
    func.argtypes = (ctypes.c_double,)
    func.restype = ctypes.c_double
    return func

sin_func = make_wrapper('sin')

# We can now call the function using Python arguments
sin_func(1.0)

# We can also call the function using ctypes arguments
sin_func(ctypes.c_double(1.0))

# We can also create a wrapper function that takes and returns Python objects
sin_func_py = FUNTYPE(sin_func)
sin_func_py(1.0)

# We can also pass a ctypes function as a callback to another c function
c.call_sin(sin_func, 1.0)

# We can also pass a Python function as a callback to another c function
c.call_sin(sin_func_py, 1.0)

# We can also wrap the callback function in a Python object
class SinFunc
