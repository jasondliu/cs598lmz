import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object(None)
fun()
</code>
This raises a <code>TypeError</code> with a message like:
<code>int() argument must be a string, a bytes-like object or a number, not 'NoneType'
</code>
which is very confusing.
What is the correct way to return <code>None</code> from a callback function?


A:

This is a bug in CPython.  It is fixed in Python 3.5.  The bug report has more details, including a workaround for Python 3.4 and earlier:
<code>def fun():
    return None
fun._returns_ = ctypes.c_void_p
</code>

