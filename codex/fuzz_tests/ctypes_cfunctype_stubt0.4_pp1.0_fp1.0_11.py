import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()
</code>
This gives me the error:
<code>TypeError: an integer is required
</code>
If I use <code>ctypes.c_int</code> instead of <code>ctypes.py_object</code> I get the error:
<code>TypeError: an integer is required
</code>
How can I fix this?


A:

You can't.  The <code>CFUNCTYPE</code> function only supports a subset of the types that can be returned by a Python function.  The <code>py_object</code> type is not one of them.

