import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE: https://github.com/python/cpython/blob/3.6/Lib/ctypes/__init__.py

# ctypes.cast(obj, type)
# Cast a ctypes instance into a new ctypes type.

# The new type is given as a type object, not a class object.
# The new type must be a subtype of the old type.

# If the old type is a pointer type, the new type must be a pointer type,
# and the pointed-to type must be the same or a subtype of the old pointed-to type.

# If the old type is a pointer type, the new type must be a pointer type,
# and the pointed-to type must be the same or a subtype of the old pointed-to type.

# If the old type is a pointer type, the new type must be a pointer type,
# and the pointed-to type must be the same or a subtype of the old pointed-to type.

# If the old type is a pointer type, the new type must be a
