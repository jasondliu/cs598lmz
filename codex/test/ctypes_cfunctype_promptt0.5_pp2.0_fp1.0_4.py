import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

# void func(int a, int b)
func_type = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print("func({}, {})".format(a, b))

func_ptr = func_type(func)

func_ptr(1, 2)
