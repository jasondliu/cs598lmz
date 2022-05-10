import ctypes
ctypes.cast(0, ctypes.py_object).value

# casts a pointer to a c_void_p, which is a void pointer, which is a pointer
# to an arbitrary memory location, which is a pointer to a Python object
# which is a pointer to a pointer to a Python object, which is a pointer to
# a pointer to a pointer to a Python object, which is a pointer to a pointer
# to a pointer to a pointer to a Python object, which is a pointer to a
# pointer to a pointer to a pointer to a pointer to a Python object, which is
# a pointer to a pointer to a pointer to a pointer to a pointer to a pointer
# to a Python object, which is a pointer to a pointer to a pointer to a
# pointer to a pointer to a pointer to a pointer to a Python object, which is
# a pointer to a pointer to a pointer to a pointer to a pointer to a pointer to
# a pointer to a pointer to a Python object, which is a pointer to a pointer to
# a pointer to a pointer to a pointer to a pointer to a pointer to a pointer to
# a pointer to a Python object, which is a
