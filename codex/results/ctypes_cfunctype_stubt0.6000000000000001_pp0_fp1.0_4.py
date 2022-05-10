import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

print fun()
</code>
And this works fine. But I want to return a pointer to a C function.
How can I do this?


A:

You can't.  The <code>ctypes</code> foreign function interface does not support returning a function pointer.

