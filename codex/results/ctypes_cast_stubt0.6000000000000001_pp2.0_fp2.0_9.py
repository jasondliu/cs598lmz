import ctypes
ctypes.cast(1, ctypes.py_object)

import sys
sys.getrefcount(1)

ctypes.cast(1, ctypes.py_object).value

# We can now store this object in a list.
# This is how you get around the limitation of not being able to store arbitrary objects in a list.

l = []
l.append(ctypes.cast(1, ctypes.py_object).value)
l

# What's the difference between this and just storing integers?
# We can still store integers in the list, but now we can store arbitrary objects as well.

# We have a list, but we are missing something.
# We can't store *anything* in a list, because the list needs to know how to compare objects.
# By default, when we store integers in a list, we can sort them.
# We can't sort arbitrary objects.

# We can't sort this list.

l.sort()

# There is a way around this.
# We can create a custom comparator.

# We can create a very simple comparator, which compares objects by their
