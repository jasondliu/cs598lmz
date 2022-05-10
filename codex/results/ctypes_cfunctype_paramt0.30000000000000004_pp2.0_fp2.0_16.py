import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(a):
    print "hello from myfunc", a
    return a

f = FUNTYPE(myfunc)
f(42)
</code>
This works fine. But if I try to use a class method instead of a function, it fails:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class Foo(object):
    def myfunc(self, a):
        print "hello from myfunc", a
        return a

f = FUNTYPE(Foo.myfunc)
f(42)
</code>
This fails with:
<code>TypeError: &lt;unbound method Foo.myfunc&gt; is not a Python function
</code>
I tried to use <code>ctypes.pythonapi.PyCFunction_New</code> to create a PyCFunction from the class method, but that fails with:
<code>TypeError: &lt;unbound method Foo.myfunc&gt
