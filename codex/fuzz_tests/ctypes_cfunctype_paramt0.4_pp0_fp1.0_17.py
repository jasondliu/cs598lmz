import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Load the library and set the function prototype
lib = ctypes.CDLL("./libmylib.dylib")
lib.fun.argtypes = [ctypes.c_int, ctypes.c_int]
lib.fun.restype = ctypes.c_int

# Create a function in python that will be used as a callback
def callback(a, b):
    print("Hello from python! %d %d" % (a, b))
    return a + b

# Convert the python function to a CFUNCTYPE
cb = FUNTYPE(callback)

# Call the C function
lib.fun(1, 2, cb)
