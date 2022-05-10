import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 123

print fun()
</code>
This works fine, but the problem is that I need to pass a ctypes array to the function.
I have tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.POINTER(ctypes.c_int))
@FUNTYPE
def fun(arr):
    return arr

print fun([1,2,3])
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print fun([1,2,3])
TypeError: argument 1: &lt;type 'exceptions.TypeError'&gt;: wrong type
</code>
I have also tried:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.POINTER(ctypes.c_int))
@FUNTYPE
def fun(arr):
    return arr

a = ctypes.
