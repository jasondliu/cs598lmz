import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

class cls:
    @FUNTYPE
    def fun(self):
        return 1

obj = cls()
print(obj.fun())
print(fun())

# Pointer types can be created by calling the type itself
# The pointer type to c_int has the same layout as
# an instance of c_int
