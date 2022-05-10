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
print(list(sys.modules.values()))
# Go through the modules and look for the mangled name
for module_object in sys.modules.values():
    # ALL_CAPS names are constants
    if module_object is None: continue
    for name in dir(module_object):
        if name == '_Z5funci':
            print(module_object)
            func_type = getattr(module_object, name)
            print(func_type)
            print(func_type.__name__)
            break
# _Z5funci is the mangled name of func
# So the following tests should be equivalent
func_type(
