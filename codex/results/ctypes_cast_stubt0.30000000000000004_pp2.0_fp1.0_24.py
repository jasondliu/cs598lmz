import ctypes
ctypes.cast(0, ctypes.py_object).value

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ctypes.ArgumentError: argument 1: <class 'TypeError'>: wrong type

# This is because the value of a NULL pointer is not a Python object.
# To get a NULL pointer to a Python object, use None:

ctypes.cast(None, ctypes.py_object).value

# Output:
# None

# The ctypes module also includes a pointer() function that creates a pointer
# from a Python object.

# The pointer() function takes an argument that specifies the type of the
# pointer. The type can be any ctypes type, including a ctypes instance.
# The pointer() function returns a ctypes instance of type POINTER(type).

# The following example creates a pointer to an integer:

i = ctypes.c_int(42)
p = ctypes.pointer(i)
assert p.contents.value == 42

# You can also create a pointer to a pointer
