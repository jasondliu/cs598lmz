import ctypes
# Test ctypes.CFUNCTYPE

#
# Test normal function
#
argtypes = (ctypes.c_int, ctypes.c_int)
restype = ctypes.c_int
#
dll = ctypes.CDLL(ctypes.util.find_library("c"))
pow = dll.pow
pow.argtypes = argtypes
pow.restype = restype
#
func = ctypes.CFUNCTYPE(restype, *argtypes)
pow2 = func(("pow", dll))
#
for i in range(3):
    for j in range(3):
        assert pow(i, j) == pow2(i, j)
#
func2 = ctypes.CFUNCTYPE(restype, *argtypes)(("pow", dll))
for i in range(3):
    for j in range(3):
        assert pow(i, j) == func2(i, j)

#
# Test function with void arg
#

def mypow(x, y):
    return pow(x, y)

