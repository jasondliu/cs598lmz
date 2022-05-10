import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# To cast an integer to a pointer of some type T, use
ctypes.cast(42, ctypes.POINTER(ctypes.c_int))

# To cast a ctypes instance to a pointer of some type T, use
ctypes.cast(my_instance, ctypes.POINTER(ctypes.c_int))

# To cast a Python object to a pointer to a ctypes instance of some type T, use
ctypes.cast(my_instance, ctypes.POINTER(T))

# To cast a pointer to a ctypes instance of some type T to a pointer to a ctypes instance of some other type V, use
ctypes.cast(my_instance, ctypes.POINTER(V))

# To cast a pointer to a ctypes instance of some type T to a pointer to a Python object, use
ctypes.cast(my_instance, ctypes.POINTER(ctypes.py_object)).contents.value

# To cast a pointer to a Python object to a pointer to a ctypes instance of some type T,
