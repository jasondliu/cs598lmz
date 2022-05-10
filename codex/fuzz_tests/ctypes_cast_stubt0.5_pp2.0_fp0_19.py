import ctypes
ctypes.cast(address, ctypes.py_object).value = value
</code>
This works, but I'm wondering if there is a more efficient way to do this.

