import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/lib/python3.5/dist-packages/ctypes/__init__.py", line 375, in __call__
    return self._function(*args)
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
I have tried to use <code>ctypes.c_int</code> instead of <code>ctypes.py_object</code> but I get the same error.
I am using Python 3.5.2 on Ubuntu 16.04.


A:

The problem is that <code>ctypes.py_object</code> is not a valid return type.  You can use <code>ctypes.py_object</code> for arguments, but not for return values.  You can use <code>ctypes.c_void_p</code>
