import ctypes
ctypes.cast(dk_obj.dk_ptr, ctypes.py_object).value

# ctypes.cast will truncate the address to 32 bits on 32bit Python
# so you must use ctypes.c_void_p() instead of ctypes.py_object()
ctypes.cast(dk_obj.dk_ptr, ctypes.c_void_p).value

# id() returns the address of an object
id(obj)
</code>

