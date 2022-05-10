import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun():
    return "world"

print(fun())
</code>
The output is "hello". I want to know why the second definition of <code>fun</code> is not used.


A:

The reason is that the first <code>fun</code> is a C function, and the second is a Python function. Python functions cannot override C functions.

