import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ()
fun()
</code>


A:

<code>ctypes.CFUNCTYPE(ctypes.py_object)</code> declares a pointer to a calling convention (the <code>CFUNCTYPE</code>) within which you can return <code>ctypes.py_object</code> (a Python object).
So when you assign a function to a pointer to a function, that function must take no arguments, and return a Python object:
<code>@FUNTYPE
def fun():
    return ()
</code>
The final line is required to bind the created pointer to the function object (but isn't really necessary), and will cause the function to be called.

