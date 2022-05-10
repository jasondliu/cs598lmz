import ctypes
ctypes.cast(0, ctypes.py_object).value

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: NULL pointer access

# ctypes.cast(0, ctypes.py_object).value
# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: NULL pointer access

print(ctypes.cast(0, ctypes.py_object).value)
