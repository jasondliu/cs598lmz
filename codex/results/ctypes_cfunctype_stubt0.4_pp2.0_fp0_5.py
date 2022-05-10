import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 2, in fun
TypeError: an integer is required (got type NoneType)
</code>
The problem is that <code>ctypes.py_object</code> is not a valid return type. 
I am using Python 3.5.2.
How can I fix this?


A:

<code>ctypes.py_object</code> is a pointer type, not a return type.  The return type is <code>ctypes.c_void_p</code>.  The <code>py_object</code> type is for passing Python objects as arguments to functions.
<code>from ctypes import *

FUNTYPE = CFUNCTYPE(c_void_p)
@FUNTYPE
def fun():
    return 42

fun()
</code>

