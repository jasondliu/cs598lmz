import ctypes
ctypes.cast(0, ctypes.py_object)

# If you have a C pointer to a Python object, you can use ctypes.cast to
# get a pointer to it.

# ctypes.cast(obj, typ)
# Converts a ctypes instance into another instance by pointing to the same
# memory block. The new instance will have the same size and alignment as typ.

# A type used for casting must be an instance of a ctypes type, or a
# pointer to such an instance.

# The new instance will have the same size and alignment as typ.

# The returned object is not a ctypes instance, and does not own the memory
# block. The original object must stay alive as long as the new object is in use.

# You cannot use this function to cast an instance of a primitive type to
# another primitive type, or to cast a pointer type to another pointer type.

# Example:

# >>> from ctypes import *

# >>> class POINT(Structure):
# ...    _fields_ = [("x", c_int),
# ...                ("y", c_int)]

