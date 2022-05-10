import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# This can be used to get the object if its id is known.
# For example, if you have a function that takes an object as an argument,
# but you only have the object's id, you can get the object back like this:

def get_object(id):
    return ctypes.cast(id, ctypes.py_object).value

# The id() function returns a unique integer for each object.
# In CPython, it is the memory address of the object.
# This is not guaranteed in other implementations of Python.
# The id() is used by the implementation to compare objects.
# The id() is different for each object.
# The id() is unique and constant for this object during its lifetime.
# Three objects with non-overlapping lifetimes may have identical ids.
# CPython implementation detail:
# CPython currently uses a scheme with two parts: the memory address and an
# integer counter. The counter is incremented whenever an object is created,
# and the address part comes from the memory allocator.
# The counter is used to
