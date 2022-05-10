import ctypes
ctypes.cast(x, ctypes.py_object).value

# Then if you want to make x point to that object again
ctypes.cast(id(x), ctypes.POINTER(y_type)).contents = ctypes.py_object(y_obj)
</code>

