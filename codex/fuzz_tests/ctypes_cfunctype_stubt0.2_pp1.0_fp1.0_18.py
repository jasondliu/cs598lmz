import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine. However, if I try to use a function that takes an argument, it doesn't work:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return x

print fun(1)
</code>
This gives the error:
<code>TypeError: fun() takes exactly 1 argument (2 given)
</code>
I've tried a few different things, but I can't figure out how to get this to work. Any ideas?


A:

<code>ctypes.CFUNCTYPE</code> is a class, so you need to instantiate it:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE()
def fun(x):
    return x

print fun(1)
</code>

