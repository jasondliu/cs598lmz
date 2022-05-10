import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# Note that the id is different from the one returned by id(int)
# because id() returns the "identity" of an object, which is guaranteed
# to be unique and constant for this object during its lifetime.
# It is the same as the object's memory address.
#
# The function id() is generally used to compute hash values and to compare
# objects by identity.
#
# All objects have identity:
#
#  - Two objects with non-overlapping lifetimes may have the same id() value.
#  - CPython implementation detail: This is the address of the object in memory.
#
# https://docs.python.org/2/library/functions.html#id

# The function ctypes.cast(obj, typ) casts the given object to the given type.
#
# https://docs.python.org/2/library/ctypes.html#ctypes.cast

# The function ctypes.py_object(obj) creates a new PyObject from the given object.
#
# https://docs.python.
