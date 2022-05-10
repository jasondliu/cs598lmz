import ctypes
ctypes.cast(ctypes.c_void_p(obj.__grefcount__), ctypes.py_object).value
</code>
Which is why <code>sys.getrefcount()</code> is not documented.

