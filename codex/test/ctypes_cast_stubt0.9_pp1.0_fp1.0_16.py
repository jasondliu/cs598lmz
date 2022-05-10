import ctypes
ctypes.cast(4, ctypes.py_object)
type(ctypes.cast(4, ctypes.py_object))
a=type(ctypes.cast(4, ctypes.py_object))

# when we use type() , it converts the datatypes
# so we need to convert it back to a list
# hence we use ctypes.py_object with our data type as list
b=ctypes.py_object(a)
