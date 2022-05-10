import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(a, b):
    return a - b

f_c = FUNTYPE(f)

print f_c(4, 5)
</code>
This gives the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    f_c = FUNTYPE(f)
  File "C:\Python26\lib\ctypes\__init__.py", line 363, in __init__
    self._flags_ = _functype_cache[restype, argtypes]
TypeError: unhashable type: 'NoneType'
</code>
Is there something wrong with the way I'm defining the function?


A:

You need to specify the return type:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
</code>

