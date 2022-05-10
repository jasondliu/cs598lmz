import ctypes
# Test ctypes.CFUNCTYPE()

def func(a, b, c):
    print(a, b, c)

# CFUNCTYPE(restype, *argtypes)
# restype: the C type of the return value
# *argtypes: a sequence specifying the C types of the arguments
#
# The returned type is callable, and will call a C function
# pointer with the specified argument and return types.
#
# When called, the returned object will create and destroy a temporary
# C array of arguments.  The arguments may be Python ints, longs,
# or floats.  The return value is usually a Python int or long, but
# can be a float or an instance of a ctypes subclass of a primitive
# type.

# The prototype of the C function must match the argtypes given,
# otherwise a TypeError exception is raised.

# The prototype of the C function must match the argtypes given,
# otherwise a TypeError exception is raised.

# The prototype of the C function must match the argtypes given,
# otherwise a TypeError exception is raised.

# The prototype of the C function must
