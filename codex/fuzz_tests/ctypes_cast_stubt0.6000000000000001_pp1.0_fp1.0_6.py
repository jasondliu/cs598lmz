import ctypes
ctypes.cast(None, ctypes.py_object)
</code>
which yields
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: expected LP_PyObject, got NoneType
</code>
I'm not sure what the best way is to fix this, but I'm happy to help.

