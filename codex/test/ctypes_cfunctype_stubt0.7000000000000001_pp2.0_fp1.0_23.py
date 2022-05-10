import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "foo"
fun()

# for testing purposes, let's try to get the function object from C to see if it's the same
# as the one we got from the class
