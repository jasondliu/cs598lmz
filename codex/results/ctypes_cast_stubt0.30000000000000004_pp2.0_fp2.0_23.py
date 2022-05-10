import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
This works fine on Python 2.7, but on Python 3.3 I get a <code>TypeError</code>:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: expected LP_PyObject, got int
</code>
I've tried casting the integer to a pointer, but that doesn't work either:
<code>ctypes.cast(ctypes.c_void_p(0), ctypes.py_object)
</code>
<code>TypeError: expected LP_PyObject, got LP_c_void
</code>
I've also tried casting the integer to a <code>c_void_p</code> and then casting that to a <code>py_object</code>, but that doesn't work either:
<code>ctypes.cast(ctypes.c_void_p(0), ctypes.py_object)
</code>
<code>TypeError: expected LP_PyObject, got LP_
