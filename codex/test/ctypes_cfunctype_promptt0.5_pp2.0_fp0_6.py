import ctypes
# Test ctypes.CFUNCTYPE

# Setup the prototype and parameters for the callback
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Define the callback
@CALLBACKFUNC
def myCallback(i):
    print("myCallback(%d)" % i)
    return i + 1

# Define a function to take the callback as a parameter
def myFunction(cb):
    print("myFunction()")
    return cb(1)

# Call the function with the callback
i = myFunction(myCallback)
print("i = %d" % i)

# Test ctypes.POINTER

# Define a type for the pointer
myCallbackPointer = ctypes.POINTER(CALLBACKFUNC)

# Define a function to take the callback pointer as a parameter
def myFunction2(cb):
    print("myFunction2()")
    return cb[0](2)

# Call the function with the callback pointer
i = myFunction2(myCallbackPointer(myCallback))
