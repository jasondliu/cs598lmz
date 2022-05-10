import ctypes
ctypes.cast(0, ctypes.py_object).value

# The ctypes module provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.

# ctypes.cast(obj, type)
# Return a new instance of type which points to the same memory block as obj.
# The new instance will be a subclass of type.
# If type is a primitive type, obj must be an object that can be interpreted as a pointer to a memory block.
# If type is a structure or union type, obj must be a pointer to a memory block large enough to hold an instance of the type.

# ctypes.py_object
# A Python object. This is the type of the objects returned by calls to the built-in functions id(), type(),
# and repr(), and of the objects returned by the ite
