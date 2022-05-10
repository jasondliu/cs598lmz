import ctypes
ctypes.cast(c_void_p(0), ctypes.py_object).value
</code>
works on Windows with Python 3.1 and 3.2 (haven't tested others).

