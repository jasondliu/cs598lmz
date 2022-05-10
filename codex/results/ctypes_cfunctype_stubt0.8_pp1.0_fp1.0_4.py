import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 25
print(fun())
</code>
it does not work. 
I've tired to find the solution but I am unable to solve this.

