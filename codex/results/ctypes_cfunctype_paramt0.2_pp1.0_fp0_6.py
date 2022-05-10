import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print f_c(2)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    f_c = FUNTYPE(f)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 363, in __init__
    self._flags_ = _FUNCFLAG_CDECL
AttributeError: 'CFUNCTYPE' object has no attribute '_flags_'
</code>
I'm using Python 2.7.3 on Ubuntu 12.04.


A:

I think you are looking for <code>ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))</code>

