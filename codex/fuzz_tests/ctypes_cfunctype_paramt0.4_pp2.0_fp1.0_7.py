import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def hello():
    print("Hello World")

# Convert the Python function to a C function pointer.
cfunc = FUNTYPE(hello)

# Call the C function pointer.
cfunc()

# Convert the Python function to a C function pointer.
cfunc = FUNTYPE(lambda: print("Hello World"))

# Call the C function pointer.
cfunc()

# Convert the Python function to a C function pointer.
cfunc = FUNTYPE(lambda x: print("Hello World {}".format(x)))

# Call the C function pointer.
cfunc(42)
</code>

