import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()

# this is the same as:

def fun():
    return "hello"

FUNTYPE(fun)

print fun()
</code>

