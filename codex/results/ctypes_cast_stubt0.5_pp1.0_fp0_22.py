import ctypes
ctypes.cast(id(int), ctypes.py_object).value
</code>
This is a bit of a hack, but it works.

