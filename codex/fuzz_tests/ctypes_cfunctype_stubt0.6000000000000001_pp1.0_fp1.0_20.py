import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun()
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.7/ctypes/__init__.py", line 378, in __call__
    return self._call_(*args)
TypeError: _call_() takes from 1 to 2 positional arguments but 3 were given
</code>
I have no idea what the third argument is, so I don't know how to fix it.
I'm using python 3.7.0 on Ubuntu 18.04.1 LTS.


A:

The third argument is the exception instance. The following works:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(exc_type, exc_val, exc_tb):
    return 1

fun(None, None, None)
</
