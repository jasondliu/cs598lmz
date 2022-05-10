import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine.
But if I try to use a function with arguments, it fails:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return x

print fun("hello")
</code>
This gives me the error:
<code>TypeError: fun() takes exactly 1 argument (2 given)
</code>
How can I use a function with arguments?


A:

You need to pass the argument to <code>CFUNCTYPE</code> as well.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return x

print fun("hello")
</code>

