import ctypes
ctypes.cast(0, ctypes.py_object).value

# should not raise AttributeError
ctypes.cast(0, ctypes.py_object).value = None
