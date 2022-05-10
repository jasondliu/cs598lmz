import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#

# This is the prototype of the function we will call:
# int double(int)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Now we get the address of the 'double' function in the _ctypes_test
# shared lib, and assign it to a Python variable.

func = prototype((_ctypes_test.__name__, "double"), ((1,),))

# The rest is the same as for function pointers in C:

for i in range(5):
    print(func(i))

#

# The prototype can also be given as a string, the names of the arguments
# don't matter:

func = prototype("int (int)")

for i in range(5):
    print(func(i))

#

# Test the error handling:

try:
    func = prototype("int (int", ((1,),))
except
