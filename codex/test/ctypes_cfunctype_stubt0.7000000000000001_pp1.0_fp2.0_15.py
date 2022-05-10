import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello world")
    return None

# Then, we specify the name of the function, and its arguments (if any)
# In this example, the extension function takes no arguments and returns an int
