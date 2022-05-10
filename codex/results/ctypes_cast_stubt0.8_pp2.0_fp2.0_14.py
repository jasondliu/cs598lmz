import ctypes
ctypes.cast(a, ctypes.c_char_p)

# ctypes.cast(input, output)
# output must be a pointer type
# input must be an object that can be interpreted as a pointer
# input is converted to a c_void_p first
# ctypes.cast(obj, type)
# Returns:
# obj converted to type. The object is not copied if no conversion is necessary.

# type must be a pointer type, or None.
# If type is a pointer type, the pointer is initialized with the object.
# If type is a pointer type or None, and the object is a pointer, the result is a new pointer to the same memory block.

# If type is None and the object is a POINTER instance, a new POINTER instance will be returned.

# If type is None, and the object is not a pointer, a new instance of the same type is returned.

# New in version 2.5.
# Changed in version 2.6: Added support for None.

# ctypes.pointer(obj)
# Return value:
# A new instance of POINTER(obj._type_)
