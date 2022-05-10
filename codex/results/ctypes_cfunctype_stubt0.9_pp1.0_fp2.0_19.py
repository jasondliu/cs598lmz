import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "foo"

print fun() # prints 'foo'
</code>

If this was called in Python, it would have thrown an exception, instead of crashing. If you want the C call to throw an exception when the Python call fails, you can use
<code>PyErr_SetString(PyExc_ValueError, "fun");
</code>

