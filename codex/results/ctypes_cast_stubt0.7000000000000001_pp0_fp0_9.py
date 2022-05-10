import ctypes
ctypes.cast(p, ctypes.py_object).value = obj
</code>
Note that <code>ctypes.cast</code> will return an object that is not directly usable by python, but rather a proxy.

