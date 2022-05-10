import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(x, y):
    return x + y

f_c = FUNTYPE(f)
print f_c(1.0, 2.0)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    f_c = FUNTYPE(f)
  File "C:\Python27\lib\ctypes\__init__.py", line 351, in __init__
    self._flags_ = _flags_
TypeError: cannot be converted to a pointer
</code>
What am I doing wrong?


A:

You can't pass a Python function to <code>ctypes</code> directly.  You need to use <code>ctypes.pythonapi.PyCFunction_NewEx</code> to get a C-compatible function pointer.
<code>from ctypes import *

FUNTYPE = CFUNCTYPE(c_double, c_
