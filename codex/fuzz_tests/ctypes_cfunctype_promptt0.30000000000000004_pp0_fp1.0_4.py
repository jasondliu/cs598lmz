import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This is a function that takes a function pointer as an argument
# and calls it.

def callback(funcptr):
    funcptr()

# This is the function we want to pass to callback

def myfunc():
    print "hello"

# Get a pointer to myfunc

myfunc_ptr = ctypes.CFUNCTYPE(None)(myfunc)

# Call callback with the pointer to myfunc

callback(myfunc_ptr)
