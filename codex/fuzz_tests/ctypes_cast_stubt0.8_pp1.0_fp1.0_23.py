import ctypes
ctypes.cast(0, ctypes.py_object).value
&lt;built-in method value of int object at 0x7fa2a53fa910&gt;

ctypes.cast(0, ctypes.py_object).value =  'Hello, World'
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: NULL PyObject used
</code>
But, when I try to do the same for, for instance, None:
<code>ctypes.cast(None, ctypes.py_object).value
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: expected LP_PyObject instance, NoneType found
</code>
Is there any way to cast None to not None value?
EDIT
My goal is to get PyObject from None, that would be possible to cast to int, str and any other type. I know
