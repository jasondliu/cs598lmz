import ctypes
ctypes.cast(0, ctypes.py_object).value
</code>
and
<code>&gt;&gt;&gt; ctypes.cast(0, ctypes.py_object).value = 'banana'
Traceback (most recent call last):
  File "&lt;pyshell#7&gt;", line 1, in &lt;module&gt;
    ctypes.cast(0, ctypes.py_object).value = 'banana'
ValueError: PyPy does not allow changing the object associated to NULL; it would break internal C code otherwise.
</code>

1. <code>PyPy</code> is a Python interpreter that is written in Python. It is a JIT compiler that compiles the Python code to native CPU instructions. It is not a <code>CPython</code> interpreter.

