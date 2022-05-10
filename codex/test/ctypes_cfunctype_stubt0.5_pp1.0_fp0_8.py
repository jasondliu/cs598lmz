import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return None

# Create a python function object
def pyfun():
    print("hello")
    return None

# Convert the python function object to a python object
