import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is the Python object equivalent to the integer 0.
# It's a singleton object, meaning that there is only one instance of it.
# That's why we can use is to compare it to other objects.

# We can use the built-in id function to get the memory address of an object.
# The memory address of the integer 0 is different from the memory address of the Python object 0.

id(0)
id(False)
id(None)

# The memory address of the Python object 0 is the same as the memory address of the Python object False
# and the memory address of the Python object None.

# The Python object 0 is a singleton object with the same memory address as the Python object False and the Python object None.

# The Python object 0 is a singleton object with the same memory address as the Python object False and the Python object None.

# This is the Python object equivalent to the integer 1.
# It's a singleton object, meaning that there is only one instance of it.
# That's why we can use is to compare it to other
