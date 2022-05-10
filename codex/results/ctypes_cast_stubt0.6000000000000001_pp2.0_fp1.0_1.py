import ctypes
ctypes.cast(ctypes.c_void_p(id(obj)), ctypes.py_object).value
</code>

