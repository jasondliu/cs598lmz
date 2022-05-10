import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import _ctypes_test

try:
    ctypes.CFUNCTYPE
except AttributeError:
    raise ImportError

################################################################

# a function

def func(arg):
    return arg * 2

# a function pointer

func_pointer = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

# a function pointer type

func_pointer_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# a function pointer instance

func_pointer_instance = func_pointer_type(func)

# a callable class

class Callable:
    def __call__(self, arg):
        return arg * 2

# a callable class instance

callable_instance = Callable()

# a callable class instance pointer

callable_instance_pointer = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(callable_instance)

# a
