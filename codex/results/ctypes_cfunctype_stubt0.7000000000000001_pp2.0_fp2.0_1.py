import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
ctypes.pythonapi.Py_MakePendingCalls()
</code>
And the error is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/ctypes/__init__.py", line 381, in __call__
    return self._callback(*args)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 539, in _call_function
    self._flags)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 310, in _get_errno
    return _sys.geterrno()
AttributeError: 'module' object has no attribute 'geterrno'
</code>
Here is the stack:
<code>#0  0x00007ffff6b9c6d9 in PyThreadState_GET () from /usr/lib/libpython2.7.so.1.0
#1  0
