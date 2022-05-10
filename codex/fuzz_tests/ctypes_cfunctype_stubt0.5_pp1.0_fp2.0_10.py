import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print(fun())
TypeError: 'PyCFunction' object is not callable
</code>
What am I doing wrong?
I'm using python 3.


A:

<code>ctypes.CFUNCTYPE</code> is the wrong function to use here. It's meant to create callbacks to C functions, not to create functions that return Python objects.
Use <code>ctypes.PYFUNCTYPE</code> instead.

