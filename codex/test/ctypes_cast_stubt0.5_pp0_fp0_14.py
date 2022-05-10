import ctypes
ctypes.cast(1, ctypes.py_object)

# ctypes.cast(obj, type)
# Converts a ctypes instance into a ctypes instance of another type.
#
# The type must be a pointer or array type.
# The new instance will share the underlying memory with the original instance.
# The new instance will not own the memory.
# This function is only useful if you need to cast away constness or volatility, for example.
