import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError: NULL pointer access

ctypes.cast(id(0), ctypes.py_object).value

# 0

ctypes.cast(id(None), ctypes.py_object).value

# None

ctypes.cast(id([]), ctypes.py_object).value

# []

ctypes.cast(id(''), ctypes.py_object).value

# ''

ctypes.cast(id(()), ctypes.py_object).value

# ()

ctypes.cast(id({}), ctypes.py_object).value

# {}

ctypes.cast(id(set()), ctypes.py_object).value

# set()

ctypes.cast(id(Ellipsis), ctypes.py_object).value

# Ellipsis

ctypes.cast(id(NotImplemented), ctypes.py_object).value

# NotImplemented

ctypes.cast(id(True), ctypes.py_object
