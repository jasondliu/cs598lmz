import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue15881#msg170215

# The bug causes a crash when calling PyObject_Call() with an exception set

# The bug is fixed in Python 3.4, 3.5, 3.6 and 3.7.  A backport of the fix for
# Python2.7 was released in https://github.com/python/cpython/commit/25c55e06

# We're using the workaround from https://bugs.python.org/issue15881#msg170215

# We're using ctypes to create a dummy object.  The dummy object won't be
# used, so it can be anything, as long as it's a real object (not NULL).

# The ctypes.py_object type creates a real object (it's equivalent to
# &PyBaseObject_Type in C code)

# The bug doesn't happen until you try to call PyObject_Call(), so this
# workaround shouldn't have any effect on performance,
