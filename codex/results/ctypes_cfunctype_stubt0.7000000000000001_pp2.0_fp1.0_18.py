import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 2

@jit(nopython=True)
def f(x):
    return x.f()

assert f(A(fun)) == 2
</code>
This is a little complicated, but it is not so hard to use.

