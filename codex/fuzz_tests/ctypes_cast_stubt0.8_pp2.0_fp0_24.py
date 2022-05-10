import ctypes
ctypes.cast(m.buffer_info_as_pointer, ctypes.POINTER(ctypes.c_int))
</code>
The <code>ctypes.POINTER</code> function takes a ctypes data type object and returns a ctypes type object representing a pointer to the other type.
These type objects are just variables, not constructors. You can't "call" the ctypes type object to create a new ctypes object like you do with other ctypes objects.

