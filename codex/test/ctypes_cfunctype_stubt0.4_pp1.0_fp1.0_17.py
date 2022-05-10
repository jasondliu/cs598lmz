import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

# This is the only line that is different from the example in the doc.
# It is the call to the function.
print(fun())
