import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine, but I want to be able to pass a function as an argument to <code>FUNTYPE</code>. I tried to use <code>ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)</code> but it didn't work.
Is there a way to do this?


A:

You can use <code>ctypes.PYFUNCTYPE</code> to create a callback function.
<code>import ctypes

def fun(arg):
    return "hello " + arg

FUNTYPE = ctypes.PYFUNCTYPE(ctypes.py_object, ctypes.py_object)

print(FUNTYPE(fun)("world"))
</code>

