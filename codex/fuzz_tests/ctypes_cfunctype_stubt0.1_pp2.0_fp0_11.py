import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine, but I want to be able to pass a function as an argument to <code>FUNTYPE</code>. I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(f):
    return f()

def f():
    return "hello"

print(fun(f))
</code>
But this gives me the error:
<code>TypeError: in method 'fun', argument 1 of type 'PyObject *'
</code>
I've tried a few other things, but I can't seem to get it to work. Any ideas?


A:

You need to use <code>ctypes.pythonapi</code> to call the function.
<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)

@FUNTYPE
def fun(f):
    return ctypes.pythonapi.
