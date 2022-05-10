import ctypes
ctypes.cast(None, ctypes.py_object)
</code>
This is the error:
<code>Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python37-32\lib\ctypes\__init__.py", line 361, in __init__
    self._b_base = _check_addrspace(self._b_base)
  File "C:\Users\user\AppData\Local\Programs\Python\Python37-32\lib\ctypes\__init__.py", line 769, in _check_addrspace
    raise TypeError("expected integer address, got %s" % repr(value))
TypeError: expected integer address, got None

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Users\user\AppData\Local\Programs\Python\Python37-32\lib\ctypes\__init__.py", line 364, in
