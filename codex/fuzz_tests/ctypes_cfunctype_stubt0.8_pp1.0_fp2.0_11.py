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
IntPointer = ctypes.POINTER(ctypes.c_int)
print(IntPointer)
print(IntPointer.__basicsize__)
print(IntPointer._type_)
print(IntPointer.__name__)
print(IntPointer.__mro__)
print(IntPointer.__dict__)

# The same applies to other pointer types
print()
print(ctypes.POINTER(ctypes.c_char))
print(ctypes.POINTER(ctypes.c_double))
print(ctypes.POINTER(ctypes.c_void_p))

# Pointer objects can be created by casting the address of
# a variable or by calling the pointer type with the address

