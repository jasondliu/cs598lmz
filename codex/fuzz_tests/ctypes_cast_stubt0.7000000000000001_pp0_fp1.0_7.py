import ctypes
ctypes.cast(1, ctypes.py_object)

# Null pointers can be cast to any pointer type:
ctypes.cast(None, ctypes.c_char_p)

# When casting from a integer, the value is used as the address of a memory
# location containing the value to cast from.
ctypes.cast(0x1234, ctypes.py_object).value

# When casting to a integer, the value is used as the address of a memory
# location in which to store the value to cast to.
addr = ctypes.cast(id(1), ctypes.c_void_p).value
ctypes.cast(addr, ctypes.c_int).value == 1

# When casting a pointer to an integer type, the bits of the pointer are
# copied to the integer value.
ctypes.cast(ctypes.pointer(ctypes.c_int(42)), ctypes.c_void_p).value

# When casting an integer to a pointer type, the bits of the integer value
# are copied to the pointer.
ctypes.cast(42, ctypes.c_void
