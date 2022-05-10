import ctypes
ctypes.cast(0, ctypes.py_object).value

# ctypes.cast(0, ctypes.py_object).value
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: NULL pointer access

# ctypes.cast(None, ctypes.py_object).value
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: NULL pointer access

# ctypes.cast(None, ctypes.py_object)
# <__main__.LP_PyObject object at 0x7f8f7c0b9e10>

# ctypes.cast(0, ctypes.py_object)
# <__main__.LP_PyObject object at 0x7f8f7c0b9e10>

# ctypes.cast(0, ctypes.py_object) == ctypes.cast(None, ctypes.py_object)
# True

# ctypes.cast(0, ctypes.py_object) is
