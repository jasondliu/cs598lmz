import ctypes
ctypes.cast(0, ctypes.py_object)

# prints "<class 'int'>"
print(type(ctypes.cast(0, ctypes.py_object)))

# raises TypeError: expected LP_PyObject instance instead of LP_int instance
