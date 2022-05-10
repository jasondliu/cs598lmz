import ctypes
ctypes.cast(2, ctypes.py_object)

int_array = [1, 2, 3, 4, 5]
ctypes.cast(int_array, ctypes.py_object)

ctypes.cast(None, ctypes.py_object)
