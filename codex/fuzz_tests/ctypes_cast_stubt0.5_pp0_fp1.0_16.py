import ctypes
ctypes.cast(0, ctypes.py_object)
# &lt;__main__.LP_PyObject object at 0x7f0c1f1f4888&gt;
</code>
Python 2
<code>import ctypes
ctypes.cast(0, ctypes.py_object)
# c_void_p(0)
</code>

The problem is that <code>ctypes</code> does not support Python 3.4 and later.
Python 3.4
<code>import ctypes
ctypes.cast(0, ctypes.py_object)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'py_object'
</code>

What is the best way to get the same result as <code>ctypes.cast(0, ctypes.py_object)</code> in Python 3.4 and later?


A:

You can use <code>ctypes.cast(0, ctypes.c_void_p).
