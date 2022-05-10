import ctypes
ctypes.cast(None, ctypes.py_object).value

# TypeError: NULL pointer access

# ctypes.py_object is a ctypes instance of type 'PyObject *'.
# ctypes.cast(None, ctypes.py_object) is a ctypes instance of type 'PyObject *'
# whose value is NULL.
# ctypes.cast(None, ctypes.py_object).value is a Python object whose value is
# the NULL pointer.

# The following is a simplified version of the code that raises the exception
# in the traceback:

ptr = ctypes.cast(None, ctypes.py_object)
ptr.value

# TypeError: NULL pointer access

# The following is a simplified version of the code that does not raise the
# exception:

ptr = ctypes.cast(None, ctypes.py_object)
print(ptr.value)

# None

# The problem is that the ctypes module does not check the value of the pointer
# before dereferencing it. This is a bug.

# The following is a workaround. It is not a
