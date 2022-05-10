import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5

print(fun())
</code>
This works fine, but I want to be able to pass in a function that takes an argument. I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return x

print(fun(5))
</code>
But I get the error:
<code>TypeError: fun() takes exactly 1 argument (2 given)
</code>
How can I make this work?


A:

You need to use <code>ctypes.py_object</code> as the argument type, not <code>ctypes.c_int</code>.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return x

print(fun(5))
</code>

