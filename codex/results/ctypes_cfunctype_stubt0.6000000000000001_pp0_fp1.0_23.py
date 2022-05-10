import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# The function can be called as usual
print(fun())

# The function can be converted to a bound method
# of an instance of a C class
class C(ctypes.Structure):
    pass

C._fun = FUNTYPE(fun)
c = C()
print(c.fun())

# The function can be converted to a function
# in a C module
m = ctypes.CDLL(None)
m.fun = FUNTYPE(fun)
print(m.fun())
</code>
I don't know of a way to convert a Python function to a C callback without creating a C function.

