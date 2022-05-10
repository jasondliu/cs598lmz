import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# A function that accepts an integer and returns an integer
#def myfunction(a):
#    return a + 2

# Create a python callback
#CALLBACK = FUNTYPE(myfunction)

# Now pass the function to C
#lib.call_python_function(CALLBACK)
#print("Done")
