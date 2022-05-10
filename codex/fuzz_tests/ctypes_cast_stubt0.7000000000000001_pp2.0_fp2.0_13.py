import ctypes
ctypes.cast(address, ctypes.py_object).value = value
</code>

However, this is not going to be faster than directly assigning to the <code>__dict__</code> attribute.

