import ctypes
# Test ctypes.CFUNCTYPE

libm = ctypes.CDLL(ctypes.util.find_library("m"))

# prototype a sin() function taking a double and returning a double
sin_func_type = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# get the C sin() function, and turn it into a Python callable
sin_func = sin_func_type(("sin", libm))

# call sin()
print sin_func(1.2)

# test the type
print type(sin_func)

# test the docstring
print sin_func.__doc__

# test the name
print sin_func.__name__

# test the module
print sin_func.__module__

# test the dict
print sin_func.__dict__

# test the class
print sin_func.__class__

# test the weakref
import weakref
print weakref.getweakrefcount(sin_func)
print weakref.getweakrefs(sin_func)

# test the repr
print
