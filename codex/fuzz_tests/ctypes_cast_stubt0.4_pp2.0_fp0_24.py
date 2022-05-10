import ctypes
ctypes.cast(id(obj), ctypes.py_object).value
</code>
This is a bit of a hack, but it does work.

