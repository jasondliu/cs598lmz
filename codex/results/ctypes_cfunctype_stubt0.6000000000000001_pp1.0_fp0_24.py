import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def f():
    return fun()

f()
</code>
This yields the error:
<code>TypeError: Don't know how to convert C return value of type int to a Python value.
</code>
I don't understand why this is the case, because the type of the C function is <code>CFUNCTYPE(py_object)</code>.


A:

I got it to work by changing the type to <code>CFUNCTYPE(ctypes.c_int)</code> and then calling <code>ctypes.pythonapi.PyInt_FromLong</code> in the C function.

