import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
</code>
This works fine, but I would like to be able to pass arguments to the function.
I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(arg):
    return arg
</code>
But it doesn't work. I get this error:
<code>TypeError: fun() takes exactly 1 argument (2 given)
</code>
I tried to use the <code>ctypes.c_int</code> type, but it doesn't work either.
I'm using Python 2.7.


A:

The problem is that the <code>CFUNCTYPE</code> decorator is not a decorator at all, but a function that returns a decorator.  So you need to do this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE()
def fun(arg):
    return arg
</code>

