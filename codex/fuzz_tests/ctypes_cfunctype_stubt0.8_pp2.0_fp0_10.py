import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return list(range(10))
A.emptyfun.argtypes = [FUNTYPE]
B.emptyfun.argtypes = [FUNTYPE]

a = A()
b = B()
a.emptyfun(fun) # So far so good
b.emptyfun(fun) # &lt;-- TypeError: in method 'emptyfun', argument 1 of type 'bfunct_t'
</code>
Is that by design?

