import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.py_object)]

a = A()
a.a = fun
a.a.__name__ = "hello"
print a.a.__name__
</code>

Solution 2 - use funcsigs in Python 2 (instead of inspect)
from http://www.saltycrane.com/blog/2010/09/python-funcsigs-multiline-lambda-workaround/
<code>from funcsigs import signature

print signature(fun)
</code>

