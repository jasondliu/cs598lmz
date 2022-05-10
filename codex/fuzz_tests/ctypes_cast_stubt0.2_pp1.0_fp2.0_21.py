import ctypes
ctypes.cast(0, ctypes.py_object).value

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: NULL pointer access

# The ctypes module provides a way to access C code from Python.
# The ctypes.cast() function takes a Python object and the type to which it is to be cast and returns a new reference to the object with the specified type.
# The ctypes.py_object type is a wrapper around the PyObject struct defined in the Python/C API.
# The PyObject struct is a C struct that contains a reference count and a pointer to a type object.
# The PyObject struct is the underlying implementation of all Python objects.
# The ctypes.py_object type is used to pass Python objects as function arguments when calling C code from Python.
# The ctypes.cast() function is not intended to be used to cast Python objects to other Python types.
# The ctypes.cast() function is intended to be used to cast between C types.
# The ctypes.cast() function is not intended to be used to cast Python objects
