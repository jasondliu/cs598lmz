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
