import ctypes
ctypes.cast(0, ctypes.py_object).value = None

# this is needed for matplotlib to work in virtual environments
