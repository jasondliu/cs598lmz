import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_long)
def myfunc(a):
    return a + 1
mypyfunc = FUNTYPE(myfunc)
mypyfunc(5)

# ctypes.py_object
# This is a Python object, representing the C void pointer PyObject* type.
# It can be used to pass arbitrary Python objects to C.
# When a ctypes.py_object is passed as an argument to a foreign function,
# it is converted to a C void pointer.
# When a ctypes.py_object is returned from a foreign function,
# it is converted back to a Python object.

# ctypes.py_object is used to implement the Python object calling protocol.
# When a callback function is called by a foreign function,
# the arguments to the callback are converted to Python objects,
# and passed to the Python callback as a tuple.
# The callback function should return a Python object.
# If the callback function returns None, the result of the callback
# is converted to a C NULL pointer.

# ctypes.structure
# This is a base class for all structure
