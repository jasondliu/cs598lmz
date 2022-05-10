import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(i):
    return i + 1

cfunc = FUNTYPE(func)

print cfunc(1)
</code>
I'm getting the following error:
<code>Traceback (most recent call last):
  File "C:\Users\Raj\Desktop\test.py", line 7, in &lt;module&gt;
    cfunc = FUNTYPE(func)
  File "C:\Python27\lib\ctypes\__init__.py", line 375, in __init__
    self._flags_ = _FUNCFLAG_CDECL
AttributeError: 'CFUNCTYPE' object has no attribute '_flags_'
</code>
I'm using Python 2.7.2 and Windows 7.

