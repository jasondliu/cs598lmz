import ctypes
# Test ctypes.CFUNCTYPE

libc = ctypes.CDLL(ctypes.util.find_library("c"))

pow = libc.pow
pow.restype = ctypes.c_double
pow.argtypes = (ctypes.c_double, ctypes.c_double)

for i in range(5):
    print pow(2.0, i)

## 2.0
## 4.0
## 8.0
## 16.0
## 32.0
## Test ctypes.CFUNCTYPE

libc = ctypes.CDLL(ctypes.util.find_library("c"))

pow = libc.pow
pow.restype = ctypes.c_double
pow.argtypes = (ctypes.c_double, ctypes.c_double)

c_pow = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

for i in range(5):
    print c_pow(2.0, i)

## 2
