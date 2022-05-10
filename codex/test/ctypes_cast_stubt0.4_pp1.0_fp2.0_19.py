import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# To cast an integer to a pointer of some type T, use
ctypes.cast(42, ctypes.POINTER(ctypes.c_int))

# To cast a ctypes instance to a pointer of some type T, use
