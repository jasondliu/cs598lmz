import ctypes
ctypes.cast(id(obj), ctypes.py_object).value
</code>
However, this is not guaranteed to work, and you should use it only if you know what you are doing.

