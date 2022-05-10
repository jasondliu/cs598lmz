import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun.__name__ = 'fun'
fun.__module__ = '__main__'

def fun():
    return 1

fun.__name__ = 'fun'
fun.__module__ = '__main__'

import timeit

t1 = timeit.timeit('fun()', 'from __main__ import fun', number=100000)
t2 = timeit.timeit('fun()', 'from __main__ import fun', number=100000)

print(t1, t2)
