import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print fun()

class Foo(object):
    def __init__(self, fun):
        self.fun = fun

f = Foo(fun)

print f.fun()
</code>
The result is:
<code>42
42
</code>

