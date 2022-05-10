import ctypes
# Test ctypes.CFUNCTYPE
def func(x): return x + 2
# Do this first, to make it possible to find the mangled name
ctypes.CFUNCTYPE(ctypes.c_int)(func)
# Call the function to make sure it is found in the module list
func(10)
# Now back to the interpreter
# First the output of Pyston
import traceback
# A list of all module objects (not their contents, just the instances)
