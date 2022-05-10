import ctypes
ctypes.cast(ctypes.addressof(ctypes.c_int(1)), ctypes.POINTER(ctypes.c_char))

# The address of a Python object can't be taken.
ctypes.cast(ctypes.addressof(ctypes.c_int(1)), ctypes.POINTER(ctypes.py_object))

# Casting an integer to a pointer type works.
ctypes.cast(42, ctypes.POINTER(ctypes.c_int))

# Casting an integer to a non-pointer type fails.
ctypes.cast(42, ctypes.c_int)

# Casting an integer to a non-pointer type fails.
ctypes.cast(42, ctypes.py_object)

# Casting an integer to a non-pointer type fails.
ctypes.cast(42, ctypes.c_char)

# Casting an integer to a non-pointer type fails.
ctypes.cast(42, ctypes.c_char_p)

# Casting an integer to a non-pointer type fails.
ctypes.cast(42, ctypes.c
