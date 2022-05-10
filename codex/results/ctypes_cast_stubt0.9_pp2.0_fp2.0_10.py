import ctypes
ctypes.cast(id(a), ctypes.py_object).value = b
</code>
But I would not recommend doing that :-)

