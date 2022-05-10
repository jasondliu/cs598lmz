import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

print(fun())
</code>
This works fine, but I can't get it to work with a function that takes an argument.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(a):
    return a

print(fun(1))
</code>
This gives me the error:
<code>TypeError: fun() takes exactly 1 argument (2 given)
</code>
I've tried a few different things, but I can't seem to get it to work.  I'm using Python 2.7.


A:

The problem is that <code>ctypes.py_object</code> is not a valid argument type for <code>CFUNCTYPE</code>.  It's a return type only.  You need to use <code>ctypes.c_void_p</code> instead.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_void_p
