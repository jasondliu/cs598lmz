import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

cfunc = FUNTYPE(func)
print cfunc(2)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    cfunc = FUNTYPE(func)
TypeError: item 1 in _argtypes_ passes a union by value, which is unsupported.
</code>
I've tried to look up the error, but I can't find anything.  I'm using Python 2.7.3 on Ubuntu 12.04.


A:

You need to specify the return type of the function.
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
</code>
should be
<code>FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
</code>

