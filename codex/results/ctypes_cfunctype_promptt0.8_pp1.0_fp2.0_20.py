import ctypes
# Test ctypes.CFUNCTYPE.

import ctypes

PYFUNCTYPE = ctypes.CFUNCTYPE

if PYFUNCTYPE is ctypes.PYFUNCTYPE:
    print("test_ctypes.py needs fixin'")
    raise SYSEXIT

# ctypes.CFUNCTYPE(void)(None) # NULLFUNC

def callback_func(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
    # print(a, b, c, d, e, f, g, h, i, j)
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p

CALLBACKFUNC = PYFUNCTYPE(ctypes.c_int,
                          ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                          ctypes.c_int, ctypes.c_int, ctypes
