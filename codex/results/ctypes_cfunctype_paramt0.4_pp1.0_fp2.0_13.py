import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return x+1

cfunc = FUNTYPE(f)
print cfunc(1)
</code>
This code works fine.
Now, I want to use a function from a shared library.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib = ctypes.cdll.LoadLibrary("libtest.so")
cfunc = FUNTYPE(lib.f)
print cfunc(1)
</code>
This code gives the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    cfunc = FUNTYPE(lib.f)
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: Don't know how to convert parameter 1
</code>
I have tried to use <code>ctypes.CFUNCTYPE(ctypes.c_
