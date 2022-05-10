import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "foo"

@jit
def f(n):
    return fun()

print(f(3))
</code>
<code>foo</code> is returned, since the <code>jit</code> converts the <code>fun</code> into a <code>ctypes</code> object that <code>numba</code> can use.

