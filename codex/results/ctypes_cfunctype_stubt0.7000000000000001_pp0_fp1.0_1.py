import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    for i in range(10000):
        pass
    return i

t0 = time()
fun()
print(time() - t0)

import numba

@numba.jit
def fun():
    for i in range(10000):
        pass
    return i

t0 = time()
fun()
print(time() - t0)

from numba import generated_jit, types
@generated_jit
def fun(a, b):
    assert a == 'foo'
    if isinstance(b, types.Integer):
        def impl(a, b):
            return a + b
    else:
        def impl(a, b):
            return a + b.upper()
    return impl

print(fun('foo', 'bar'))
print(fun(1, 2))

from numba import float64, int64, complex128
from numba.extending import register_jitable
@register_jitable
def add(a, b):
    return a + b

@register_jitable
def mul(a, b):
   
