import ctypes
ctypes.cast(0, ctypes.py_object)

# This is the only way to get a reference to the current interpreter.
# We need to store this in a global variable, so that we can pass it
# to other threads.
