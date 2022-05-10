import ctypes
# Test ctypes.CFUNCTYPE in the pure Python implementation
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def cmpfunc(int1, int2):
    return int1-int2
qsort  = ctypes.pythonapi.qsort
qsort.argtypes = [ctypes.c_voidp,
                  ctypes.c_int,
                  ctypes.c_int,
                  CMPFUNC]
array =  (ctypes.c_int * 10)()
for idx, value in enumerate((3,1,7,0,4,2,5,9,8,6)):
    array[idx] = value
