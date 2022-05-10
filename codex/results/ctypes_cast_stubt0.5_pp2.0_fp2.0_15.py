import ctypes
ctypes.cast(12, ctypes.py_object)

# The returned object is a Python "long", which is different from the normal
# "int" type.  It's just a historical accident.  "long" has been renamed to
# "int" in Python 3.0.

# The function "id()" returns the identity of an object as an integer.  This
# integer is guaranteed to be unique and constant for this object during its
# lifetime.  Two objects with non-overlapping lifetimes may have the same id()
# value.

# CPython implementation detail: This is the address of the object in memory.

id(None)
id(True)
id(5)

# The function "type()" returns the type of the object.  Like "id()", the
# return value is generally an integer, but unlike "id()", which is guaranteed
# to be unique, the return value from "type()" is not necessarily unique
# among the different objects.  "type()" is not a function but actually a
# meta-type; it is possible to override the behavior of "type()" for a class
