import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "foo"
fun()

# for testing purposes, let's try to get the function object from C to see if it's the same
# as the one we got from the class
FUNTYPE(fun.__dict__['_C_function'])  # this is the one from C

# let's see if it's the same as the original one
# the following is not okay but that's python
#fun.__dict__['_C_function'] is fun
#fun.__dict__['_C_function'] is FUNTYPE(fun.__dict__['_C_function'])  # yes it is!

# okay, so we have the function pointer in the __dict__ of the original function
# it's the same as the one we got from C
# so that's something, but it's still not the original function...

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "foo"

# let's get the function pointer from the function
# this is the correct way to get the function pointer from
