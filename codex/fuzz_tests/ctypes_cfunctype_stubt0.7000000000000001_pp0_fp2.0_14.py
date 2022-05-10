import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

class A():
    def __init__(self):
        self.x = 1

a = A()
a.fun = fun

a.fun()
</code>
But on PyPy, this fails with:
<code>Traceback (most recent call last):
  File "test.py", line 18, in &lt;module&gt;
    a.fun()
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: expected LP_c_object_p instance instead of int
</code>
Doing the same thing with a normal function, i.e. without <code>ctypes</code> works fine.
I've tried using the <code>ctypes.c_void_p.from_address</code> function, but that doesn't help:
<code>pfun = ctypes.c_void_p.from_address(id(fun))
</code>
If I try to assign the <code>pfun</code> directly to the object, it works only once:
<code>a.fun = pfun
