import ctypes
# Test ctypes.CFUNCTYPE
def baz(x, y):
    return x, y

PFUN = ctypes.CFUNCTYPE(ctypes.c_int,   # return type
                        ctypes.c_int,   # arg1 type
                        ctypes.c_int)   # arg2 type

# Now create an instance of the function
pfun = PFUN(baz)

# Use it!
print(pfun(3,4))

print(pfun.__name__)

# Compile it?
import Cython.Compiler.Options 
Cython.Compiler.Options.annotate = True
import pyximport
pyximport.install()

import hello2

print(hello2.__file__)
print(hello2.pfun(3,4))


# import pyximport
# pyximport.install(setup_args={'include_dirs': [np.get_include()]},
#                   inplace=True)

# import my_module


import intermodule
import intermodule2

print(" -> ".join([intermodule
