import ctypes
ctypes.cast(ctypes.c_void_p(0x12345678), ctypes.POINTER(ctypes.c_int))

# ctypes.cast(obj, typ)
# Converts a ctypes instance into a ctypes instance of another type.
# The new instance will use the same memory block, so that modifying
# one modifies the other.

# ctypes.c_void_p(obj)
# Creates a ctypes instance of type c_void_p from the given object.
# If the object is an integer or a c_void_p instance, the new instance
# will point to the same memory location.

# ctypes.POINTER(typ)
# Returns a new type representing a pointer to typ.

# ctypes.c_int
# A ctypes type representing a C int.

# ctypes.c_void_p
# A ctypes type representing a C void pointer.

# ctypes.addressof(obj)
# Returns the memory address of the given ctypes instance obj.

# ctypes.byref(obj)
# Returns a ctypes pointer to
