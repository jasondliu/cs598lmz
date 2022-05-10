import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def py_func(x):
    print(x)

cfunc = FUNTYPE(py_func)
cfunc(1)
</code>
This code works fine and prints <code>1</code> in the python console. But when I try to use an <code>int</code> type for the argument of the function, it fails:
<code>def py_func(x: int):
    print(x)

cfunc = FUNTYPE(py_func)
cfunc(1)
</code>
The error I get is:
<code>TypeError: &lt;class 'TypeError'&gt;: Don't know how to convert parameter 1
</code>
I am using Python 3.6.4.

