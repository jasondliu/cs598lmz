import ctypes
ctypes.cast(ctypes.c_void_p(0x1), ctypes.c_void_p)
</code>
But I get an error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: NULL pointer access
</code>
How can I cast a <code>Py_uintptr_t</code> to a <code>PyObject*</code>?


A:

If you are trying to get a pointer to a Python object, you can use <code>PyObject_FromVoidPtr</code>.

