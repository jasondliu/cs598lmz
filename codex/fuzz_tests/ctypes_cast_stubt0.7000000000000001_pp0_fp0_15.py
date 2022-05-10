import ctypes
ctypes.cast(ptr, ctypes.py_object).value
</code>
This is the only way to get a pointer to a Python object in C and back to Python.
(Cython uses a similar approach to get the actual Python objects behind its <code>object</code> type.)

