import ctypes
ctypes.cast(0, ctypes.py_object).value

# The ctypes module is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.

# The ctypes module provides the following functions:

# ctypes.cast(obj, type)
# Cast a ctypes instance into a ctypes instance of another type.

# ctypes.POINTER(type)
# Create a new pointer type to the given type.

# ctypes.pointer(obj)
# Return a new pointer instance to the given ctypes instance.

# ctypes.addressof(obj)
# Return the address of the given ctypes instance.

# ctypes.byref(obj[, offset])
# Return a pointer to the given ctypes instance.

# ctypes.string_at(ptr[, size])
# Return a string containing the contents of the memory block pointed to by ptr.

# ctypes.wstring_at(ptr[, size])
# Return a unicode string containing the contents of the memory block
