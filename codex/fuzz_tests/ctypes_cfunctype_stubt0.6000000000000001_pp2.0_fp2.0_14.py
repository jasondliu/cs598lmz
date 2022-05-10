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
</code>
The result is
<code>0.03643430000082414 0.038172900000176404
</code>
So the first version is faster.
The difference is not so big and depends on the platform. 
I tested on Windows 7 and Python 3.4.2

