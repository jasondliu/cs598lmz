import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

fun()
</code>
The above code works because the return type of <code>fun</code> is <code>ctypes.py_object</code> which is a pointer to a <code>PyObject</code>. 
I want to make this work with a <code>tuple</code> as the return type. So I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return (x,1)

fun(1)
</code>
Which fails with the following error:
<code>TypeError: expected a string or other character buffer object
</code>
Is there a way to make this work?


A:

The problem is that <code>ctypes.py_object</code> is a pointer to a <code>PyObject</code>, not a <code>PyObject</code> itself.  You'll need to use <code>ctypes.py_object.from_param()</code> to
