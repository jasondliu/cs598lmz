import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# The ctypes.cast() function can be used to cast a ctypes type to any other type.

# The ctypes.pythonapi module contains a number of functions and variables that can be used to access Python C API functions.

# For example, the following code calls the PyObject_Str() function, which returns a Python string object from the given object:

import ctypes

# Load the shared library into ctypes.
lib = ctypes.CDLL('./libsample.so')

# Set the argtypes for the function 'pystring_from_string'.
lib.pystring_from_string.argtypes = [ctypes.c_char_p]

# Set the restype to be a Python object.
lib.pystring_from_string.restype = ctypes.py_object

# Call the function.
result = lib.pystring_from_string(b'Hello World!')

# Print the result.
print(result)

# The ctypes.pythonapi module also contains a number of variables that can be used
