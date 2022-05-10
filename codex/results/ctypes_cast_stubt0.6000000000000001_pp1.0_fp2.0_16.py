import ctypes
ctypes.cast(p, ctypes.py_object).value

# Example:
# >>> import ctypes
# >>> a = [1,2,3]
# >>> ctypes.cast(id(a),ctypes.py_object).value
# [1, 2, 3]
# >>> ctypes.cast(id(a),ctypes.py_object).value is a
# True
# >>> ctypes.cast(id(a),ctypes.py_object).value == a
# True

# If you have a pointer to an object,
# you can get the object by casting the pointer to a py_object,
# and then accessing the value attribute of the py_object.
# This is not very useful in Python, but could be useful in Cython
# if you want to access a Python object pointer from
# within a C context.

# Note that this trick is not guaranteed to work on every platform
# and every Python implementation.
# It works on CPython 2.6/2.7, but not 3.2.
# It works on PyPy 1.6, but not 1.5.
