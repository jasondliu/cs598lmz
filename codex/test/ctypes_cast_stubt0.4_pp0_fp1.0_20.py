import ctypes
ctypes.cast(0, ctypes.py_object)

# prints <class 'ctypes.py_object'>
print(type(ctypes.cast(0, ctypes.py_object)))

# raises TypeError: an integer is required
