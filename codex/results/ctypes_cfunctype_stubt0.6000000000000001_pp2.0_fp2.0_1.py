import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
I get the error:
<code>TypeError: an integer is required (got type NoneType)
</code>
As far as I can see, the return type of <code>fun</code> is an integer, so why is it complaining that an integer is required?


A:

It's complaining because the <code>funtype</code> that you created specifies that the return type of the function is a <code>ctypes.py_object</code>.  A <code>ctypes.py_object</code> is a wrapper around a Python object and the return value of your function is <code>None</code>.  If you change the return type to <code>ctypes.c_int</code> you should be able to get around this problem.

