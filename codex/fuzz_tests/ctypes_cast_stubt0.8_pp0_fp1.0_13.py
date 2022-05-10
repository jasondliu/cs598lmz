import ctypes
ctypes.cast(id(obj), ctypes.py_object)
</code>
There is no public API to get a PyObject* from a handle, and using a private API is fragile and not guaranteed to work across Python versions or platforms.

