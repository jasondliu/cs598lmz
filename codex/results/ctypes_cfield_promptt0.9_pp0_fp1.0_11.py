import ctypes
# Test ctypes.CField and compiler.visit_Attribute.
lib = ctypes.CDLL(ctypes.util.find_library('m'))
lib.cos.restype = ctypes.c_double
ctypes.c_double.acos = lib.acos
z = 1 + 2j
cmath.acos(z)
def _acos(z):
    return ctypes.c_double.acos(z)

_acos(z)
%timeit _acos(z)
 
def f(z):
    # Should be compiled
    return ctypes.c_double.acos(z)

f(z)
%timeit f(z)
%debug
 
def g(z):
    # Should not be compiled
    return ctypes.CField(z, "real")

g(1)
%timeit g(1)
libm = np.ctypeslib.load_library('m', np.core.multiarray.__file__)
%timeit np.sqrt(3.4)
%timeit pow(3.4, 0
