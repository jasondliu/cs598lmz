import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# get the object through the memory address
a = int()
ctypes.cast(id(a), ctypes.py_object).value is a

# get the value
ctypes.cast(id(a), ctypes.py_object).value

# get the value's memory address
id(ctypes.cast(id(a), ctypes.py_object).value)


# isinstance(obj, class_or_tuple)
# Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns false.
# If classinfo is a tuple of type objects (or recursively, other such tuples), return true if object is an instance of any of the types.
# If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.
# Changed in version 3.2: Support for multiple inheritance.

# issubclass(class, class_or_tuple)
#
