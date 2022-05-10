import ctypes
ctypes.cast(0, ctypes.py_object).value

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: NULL pointer access

# This is because the value attribute is a Python object, which is not allowed to be None.

# The from_address() function can be used as an alternative, which returns a ctypes instance
# representing the memory address, instead of the value stored there.

# Example
import ctypes
ctypes.cast(id(ctypes.c_int(42)), ctypes.py_object).value

# Output:
# 42

# The from_address() function is also useful for creating a ctypes instance from a pointer to
# a C structure.

# Example
import ctypes
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(10, 20)
print(point.x, point.y)

# Output:
# 10 20
