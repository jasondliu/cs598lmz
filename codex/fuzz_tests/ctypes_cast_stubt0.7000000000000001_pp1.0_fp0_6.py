import ctypes
ctypes.cast(1, ctypes.py_object)

# In this case, the object was created by Python.
# It is a simple integer, and its address is immutable.

# Now, when we cast the integer 1 to type py_object,
# the C object stores a pointer to the Python object.
# The C code is now responsible for the lifetime of the Python object.

# Let's see what happens when the integer is garbage collected.

sys.getrefcount(1)

# 3: one from the integer itself,
# one temporary reference from sys.getrefcount,
# and one from the C object.

# Now, let's delete the temporary reference from sys.getrefcount.

del sys

# The integer is now unreachable, so it is garbage collected.

# If you run this script with Python 2.7,
# you will get a Segmentation fault at this point,
# because the C object still points to the integer,
# which has been deallocated.

# In general, the C object will keep the Python object alive,
# but the Python object won't keep the C object
