import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
fun()
type(fun)
from numba import cfunc
from numba.types import int32

@cfunc(int32)
def fun():
    return 1
type(fun)
print(hex(id(fun)))
from numpy import array
from numba import cfunc
from numba.types import int32, int64

@cfunc(int64[:](int32[:]))
def fun(array):
    return array
type(fun)
hex(id(fun))
fun = cfunc('int64(int32[:])')(lambda array: array)

type(fun)
 
from numba.types import int64, int32
from numba.decorators import cfunc, jit
from numba import deferrable_type, deferred_type
@cfunc(int64(int32, int64))
def fun(a, b):
    return a + b

@jit()
def test(a, b):
    return fun(a, b)
print(hex(id(test)))
test(1, 2
