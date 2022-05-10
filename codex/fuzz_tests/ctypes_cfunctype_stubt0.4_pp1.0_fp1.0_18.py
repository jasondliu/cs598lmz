import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()
</code>
The error is:
<code>TypeError: Don't know how to convert parameter 1
</code>
I'm using Python 3.7.4 on Windows 10.
I've tried to use the <code>ctypes.c_void_p</code> type as the return type, but it didn't work.
What is the correct return type to use?


A:

I think you need to use <code>ctypes.py_object</code> as the return type.
<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>

