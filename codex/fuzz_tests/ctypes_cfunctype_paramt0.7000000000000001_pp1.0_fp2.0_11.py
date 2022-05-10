import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def cfunc(f):
    """Compile a Python function f into a ctypes CFUNCTYPE"""
    return FUNTYPE(f)

# Now we create a libary of compiled functions using this decorator.
# This is a singleton, so that we don't recompile the library on each
# call.
class Library(object):
    def __init__(self):
        self.lib = {}
    def __call__(self, f):
        if not f.__name__ in self.lib:
            self.lib[f.__name__] = cfunc(f)
        return self.lib[f.__name__]

# Create the singleton library.
library = Library()

# And define our two functions as decorated ctypes functions.
@library
def f(x):
    return x**2

@library
def g(x):
    return x**3

# Now we can call our functions as normal Python functions, but they
# are compiled to ctypes.
f(2)
