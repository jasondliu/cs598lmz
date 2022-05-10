import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun()
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "&lt;pyshell#10&gt;", line 1, in &lt;module&gt;
    fun()
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: Don't know how to convert parameter 1
</code>


A:

That's because, when the C function returns, it returns to the caller. In this case, the caller is the Python interpreter.
The Python interpreter has no idea what to do with a C <code>int</code>, so it raises the exception you see.
Also, in the 32-bit Windows version of Python, the return value from a C function must be a C <code>long</code>, not an <code>int</code>.
<code>from ctypes import *

FUNTYPE = CFUNCTYPE(c_long)
@FUNTYPE
def fun():
    return 1

print fun() # prints 1
</code>

