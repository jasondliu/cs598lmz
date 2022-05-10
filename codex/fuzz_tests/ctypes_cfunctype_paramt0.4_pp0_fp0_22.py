import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# Load the library
lib = ctypes.CDLL("./libtest.so")

# Set the return type of the function
lib.test.restype = None

# Set the argument type of the function
lib.test.argtypes = [FUNTYPE]

# Define the callback function
def my_callback():
    print("Hello from Python")

# Convert the Python function into a C function
cfunc = FUNTYPE(my_callback)

# Call the C function
lib.test(cfunc)
</code>

