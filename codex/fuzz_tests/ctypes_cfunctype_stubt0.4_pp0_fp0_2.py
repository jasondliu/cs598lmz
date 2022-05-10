import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return None
fun()
</code>
This raises an exception:
<code>TypeError: cannot return None unless the callable returns a pointer
</code>
I'm using Python 3.4.1 on Windows 7.
I know that the <code>ctypes</code> documentation says that the function should return a <code>c_void_p</code>, but I don't know how to do that.
Edit: I'm using <code>ctypes</code> because I want to use a C library in Python.


A:

You can't return <code>None</code> from a <code>CFUNCTYPE</code> function. You must return a <code>c_void_p</code> instance.
<code>from ctypes import *

FUNTYPE = CFUNCTYPE(c_void_p)

@FUNTYPE
def fun():
    return None

fun()
</code>

