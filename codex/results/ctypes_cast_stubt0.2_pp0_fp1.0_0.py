import ctypes
ctypes.cast(0, ctypes.py_object)

# ctypes.cast(obj, type)
# Cast an object to a type.
# The return value is the object passed as obj with the type changed to type.
# The new type must be a pointer type.

# ctypes.py_object
# The type of Python objects.
# This type is used to pass Python objects to and from C.
# It is also used to represent the result of a function that returns a Python object.

# ctypes.POINTER(type)
# Return a new type representing a pointer to type.
# type must be a ctypes type, such as c_int.
# The new type is a subtype of the type of the pointer returned by the built-in function id().
# The new type is callable, and calls the function pointed to by the pointer.

# ctypes.byref(obj[, offset])
# Return a ctypes object that has a pointer to obj.
# The object will have the same type as obj, unless obj is a pointer.
# In that case, the type of the returned object will be a pointer to
