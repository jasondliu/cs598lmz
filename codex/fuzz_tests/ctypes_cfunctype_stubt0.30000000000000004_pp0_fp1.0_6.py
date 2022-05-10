import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"
</code>
But I get the following error:
<code>TypeError: item 1 in _argtypes_ passes a union by value, which is unsupported.
</code>
I am using Python 3.7.1 on Windows 10.

