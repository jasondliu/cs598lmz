import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print(a, b)
    return a + b

cfunc = FUNTYPE(myfunc)

print(cfunc(1, 2))
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    cfunc = FUNTYPE(myfunc)
TypeError: must be real number, not function
</code>
I'm using Python 3.7.2 on Windows 10.

