import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
This works fine, but I don't know how to pass arguments to the function. I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return x

fun("hello")
</code>
But this gives a <code>TypeError: expected LP_CFUNCTYPE instance instead of str</code>.
I also tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return x

fun(ctypes.py_object("hello"))
</code>
But this gives <code>TypeError: expected LP_CFUNCTYPE instance instead of py_object</code>.
How can I pass arguments to the function?


A:

The problem is that <code>ctypes.py_object</code> is a type, not a
