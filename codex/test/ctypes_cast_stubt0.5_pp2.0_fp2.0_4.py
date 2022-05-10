import ctypes
ctypes.cast("Hello", ctypes.py_object)

# for example, if you have a C function configured to accept a C 'double',
# you can pass a Python float directly to it.
