import ctypes
# Test ctypes.CFUNCTYPE
def func(a,b):
    return a+b

#CFUNCTYPE(restype, *argtypes)
#restype is a C type, or a Python callable.
#argtypes is a list of C types.
#The function call operator is then used to create a callable object.

#CFUNCTYPE(c_int, c_int, c_int) == c_int(c_int, c_int)
#c_int(c_int, c_int) is a type object, representing the C type int(*)(int, int).
#The CFUNCTYPE function returns a callable object that, when called, creates and returns a new function object.
#The function object is callable, and takes the arguments specified by argtypes.
#The function object also includes a __restype__ attribute, which is the type specified by restype.
#This is used by ctypes to determine the type of the result of calling the function.

#If restype is a Python callable, it is called with one argument, the integer return value of the function,
#and should
