import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hi"
</code>
I tried this and I get this error:
<code>ValueError: Procedure called with not enough arguments (4 bytes missing) or wrong calling convention
</code>
How can I return a string from a function in Python?


A:

The following works:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)
@FUNTYPE
def fun():
    return "hi"
</code>
The return type of the function must be <code>c_void_p</code>.

