import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

class Foo(object):
    def __init__(self, a):
        self._a = a

    def __call__(self, x):
        return self._a + x

def foo(x):
    return x + 1

foo_obj = Foo(1)

# this works
f = FUNTYPE(foo)

# this works
f = FUNTYPE(foo_obj)

# this does not work
f = FUNTYPE(foo_obj.__call__)
</code>
The last line throws an exception:
<code>TypeError: expected CFUNCTYPE instance, got instancemethod
</code>
I was wondering if there is a way to get around this? I know that I can use the <code>ctypes.cast</code> function, but I was wondering if there is a better way to do this.


A:

The problem is that <code>ctypes</code> doesn't know how to convert a Python function to a C function.  You can use <code>ctypes.CFUN
