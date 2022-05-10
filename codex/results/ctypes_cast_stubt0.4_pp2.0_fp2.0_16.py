import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a Python object, a string
ctypes.cast(id(''), ctypes.py_object).value

# This is a Python object, an int
ctypes.cast(id(0), ctypes.py_object).value

# This is a Python object, a list
ctypes.cast(id([]), ctypes.py_object).value

# This is a Python object, a function
ctypes.cast(id(len), ctypes.py_object).value

# This is a Python object, a module
ctypes.cast(id(ctypes), ctypes.py_object).value

# This is a Python object, a C function
ctypes.cast(id(ctypes.cast), ctypes.py_object).value

# This is a Python object, a C type
ctypes.cast(id(ctypes.c_int), ctypes.py_object).value

# This is a Python object, a Python class
ctypes.cast(id(list), ctypes.py_object).value

