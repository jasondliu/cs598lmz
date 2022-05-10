import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(x):
    print(x)
    return x + 1

func(1)
func(2)
func(3)

