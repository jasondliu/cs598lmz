import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3
print "compiled with ctypes"
print fun()

from numba import *
print "compiled with numba"
@jit(pyobject_)
def foo():
    return 3
print foo()
</code>
This gives the following output:
<code>compiled with ctypes
3
compiled with numba
3
</code>
Ok, now let's add a more complicated example:
<code>class Bar(object):
    def __init__(self, val):
        self.val = val
    def __int__(self):
        return self.val
    def __mod__(self, other):
        return self
    def __add__(self, other):
        return self


@jit(pyobject_)
def foo():
    return Bar(3) % 2 + 1

print foo()
</code>
This gives the following output:
<code>compiled with ctypes
3
Traceback (most recent call last):
        ...
AttributeError: 'Bar' object has no attribute '__mod__'
</code>

