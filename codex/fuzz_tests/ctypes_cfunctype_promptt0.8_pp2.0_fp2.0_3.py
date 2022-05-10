import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import CFUNCTYPE
from ctypes import POINTER
from ctypes import c_double
from ctypes import c_int

prototype = CFUNCTYPE(POINTER(c_double), POINTER(c_double), c_int, c_double, c_double)
def _py_multiquadric(r, df, n, a, b):
    result = (c_double * n)()
    for i in range(n):
        result[i] = a + b * (r[i]**2)**0.5
    df[0] = a * 0.5 + b * r[0] / (r[0]**2)**0.5
    return result
multiquadric = prototype(_py_multiquadric)

# Test ctypes.PYFUNCTYPE
from ctypes import PYFUNCTYPE
from ctypes import c_float

argtypes = (c_float,)
restype = c_float
pyfunc = PYFUNCTYPE(restype, *argtypes)
callback = py
