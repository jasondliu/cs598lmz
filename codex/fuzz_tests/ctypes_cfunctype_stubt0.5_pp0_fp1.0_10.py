import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

print(fun())

# Creating a callback function
def callback(x):
    print("Callback called with {0}".format(x))

callback = FUNTYPE(callback)

# Passing a callback to a C function
lib.call_callback(callback)
