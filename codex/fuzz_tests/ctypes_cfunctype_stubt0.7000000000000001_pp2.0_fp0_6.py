import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, World"

# Create an instance of the function type
f = fun()
print(f())

# Create a FunctionType with a different signature
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
@FUNTYPE
def fun(a, b):
    return a + b

f = fun(1, 2)
print(f)

# FunctionType instances are callable directly
print(fun(1, 2))

# Creating a new instance of a FunctionType is easy
f = FUNTYPE(lambda a, b: a + b)
print(f(1, 2))

# This works even if the FunctionType is created in C
# (as long as the PyObject* returned by the function
# can be converted to a PyCFunction)

# Load the library created in test_func.c
lib = ctypes.cdll.LoadLibrary("./test_func.so")

# Get the function pointer
f = lib.get_func()

# Call the function
