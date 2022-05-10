import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print fun()
</code>
This prints 42.
But if I try to do this with a function that takes an argument, I get an error:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(a):
    return a

print fun(42)
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    print fun(42)
TypeError: argument 1: &lt;type 'exceptions.TypeError'&gt;: wrong type
</code>
I've tried a bunch of different things, but I can't figure out how to get this to work. Any suggestions?


A:

I think you need to pass the function a ctypes object.  This works:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
