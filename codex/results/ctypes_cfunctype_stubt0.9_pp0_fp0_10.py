import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
ret = fun()
</code>
<code>ctypes.cast(ctypes.py_object(fun), FUNTYPE)</code> is not a good idea, since it will convert to a different type of callable. For example, after the cast,
<code>def asd():
    print(fun())
</code>
will raise <code>TypeError: 'CArgObject' object is not callable</code>.

