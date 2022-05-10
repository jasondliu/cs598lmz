import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 10

class A(object):
    def test(self):
        pass

@functools.wraps(A.test)
def fun2(self):
    pass

class B(object):
    test = fun2

c = ctypes.cast(fun, ctypes.c_void_p).value
d = ctypes.cast(B.test, ctypes.c_void_p).value
print c
print d
print c == d
print type(fun)
print type(B.test)
print fun.__name__
print B.test.__name__
print fun.__module__
print B.test.__module__
</code>
Which outputs:
<code>140447696036288
140447696036288
True
&lt;type 'function'&gt;
&lt;type 'instancemethod'&gt;
fun
test
__main__
a
</code>
So the function is definitely not the same as the method.

