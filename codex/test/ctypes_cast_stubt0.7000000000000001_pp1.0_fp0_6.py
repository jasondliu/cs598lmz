import ctypes
ctypes.cast(1, ctypes.py_object)

# In this case, the object was created by Python.
# It is a simple integer, and its address is immutable.

# Now, when we cast the integer 1 to type py_object,
# the C object stores a pointer to the Python object.
# The C code is now responsible for the lifetime of the Python object.

# Let's see what happens when the integer is garbage collected.

