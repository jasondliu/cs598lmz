import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

print fun()
</code>
I get the following error:
<code>TypeError: CFUNCTYPE(obj) found for argument 'argtypes'
</code>
I am using Python 2.7.12.
Any help would be appreciated.


A:

You can't return a Python object from a C function, unless you explicitly allocate it on the heap and manage its lifetime. 
You can return a C <code>char*</code> to a Python string, but that's it.

