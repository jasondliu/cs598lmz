import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
</code>
This gives the error:
<code>TypeError: an integer is required
</code>
If I omit the <code>return 0</code> line, the error becomes:
<code>TypeError: an integer is required (got type NoneType)
</code>
Python 3.8.2 on Windows 10.


A:

The function type you have created is <code>ctypes.CFUNCTYPE(ctypes.py_object)</code>. This means the function must return a Python object, i.e. a reference to a Python object.
The return value <code>0</code> is not a reference to a Python object, it's an integer.
You can return a Python object by converting the integer to a reference to a Python object:
<code>@FUNTYPE
def fun():
    return ctypes.py_object(0)
</code>

