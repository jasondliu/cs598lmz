import ctypes
ctypes.cast(0, ctypes.py_object).value

# The address of the object is the same as the address of the value.
ctypes.cast(id(0), ctypes.py_object).value is 0

# The address of the object is different from the address of the value.
ctypes.cast(id([]), ctypes.py_object).value is []

# The address of the object is different from the address of the value.
ctypes.cast(id(''), ctypes.py_object).value is ''

# The address of the object is different from the address of the value.
ctypes.cast(id(()), ctypes.py_object).value is ()

# The address of the object is different from the address of the value.
ctypes.cast(id({}), ctypes.py_object).value is {}

# The address of the object is different from the address of the value.
ctypes.cast(id(set()), ctypes.py_object).value is set()

# The address of the object is different from the address of the value.
ctypes
