import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 17
obj.fun_callback(fun)
assert obj.fun_call()==17

# arguments and return value
# This has to be declared by the users of ctypeslib, like in the example
# below.  We let the user define the argument and return types.  Users
# need to think hard to decide whether they want Python types or C types
# here, they cannot mix the two.
from ctypes import c_int, c_double
c_double_p = ctypes.POINTER(c_double)
ctypeslib.ndpointer.__repr__ = lambda ct: "<ndpointer>"
ctypeslib.ndpointer.__str__ = lambda ct: "<ndpointer>"
def ndarray(ndim=None,shape=0,dtype=None):
    import numpy
    if ndim:
        return numpy.ctypeslib.ndpointer(dtype=dtype, ndim=ndim)
    else:
        return numpy.ctypeslib.ndpointer(dtype=dtype, shape=shape)

obj.foo_func.restype
