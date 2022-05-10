import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
fun()
</code>
I get the error
<code>TypeError: item 1 in _argtypes_ passes a union by value, which is unsupported.
</code>
I'm using Python 3.3.3.

