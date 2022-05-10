import ctypes
ctypes.cast(event.GetClientData(), ctypes.py_object).value
#Assumes event.GetClientData() is ctypes.cast(some_py_object, ctypes.c_void_p)
</code>
This should be in a <code>try/except</code> though, as it will not work if it does not return an object reference.

