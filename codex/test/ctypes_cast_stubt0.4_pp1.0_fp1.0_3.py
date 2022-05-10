import ctypes
ctypes.cast(0, ctypes.py_object)

# Create a new reference
ctypes.py_object(None)

# Create a new reference and steal ref
ctypes.py_object(ctypes.py_object(None))

# Create a new reference and increment ref
