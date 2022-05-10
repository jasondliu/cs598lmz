import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

@jit(nopython=True)
def test(f):
    return f()

test(fun)
</code>

