import ctypes
ctypes.cast(ptr, ctypes.py_object).value = value
</code>
This is because <code>ctypes</code> casts the pointer to a <code>void *</code> which is not a pointer to an <code>PyObject *</code> but is a pointer to anything.

