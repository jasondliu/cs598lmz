import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print fun()
</code>
This works fine, but I have no idea how to pass arguments to the function.
I tried to do the following:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(arg):
    return arg

print fun("hello world")
</code>
But this gives me the following error:
<code>TypeError: in method 'new_fun', argument 2 of type 'PyObject *'
</code>
I'm using Python 2.7.3 on Windows 7.
Any ideas?


A:

You need to pass a <code>ctypes</code> object as the second argument:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(arg):
    return arg

print fun(ctypes.py_object("hello world"))
</code>

