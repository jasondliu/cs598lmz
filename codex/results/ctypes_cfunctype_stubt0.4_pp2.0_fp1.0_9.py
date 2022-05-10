import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print fun()
</code>
I get an error:
<code>Traceback (most recent call last):
  File "C:\Users\Documents\Python\test.py", line 8, in &lt;module&gt;
    print fun()
TypeError: 'int' object is not callable
</code>
Can anyone help me?


A:

You need to return a Python object from your callback, not a C <code>int</code>.
<code>from ctypes import *

FUNTYPE = CFUNCTYPE(py_object)
@FUNTYPE
def fun():
    return 1

print fun()
</code>

