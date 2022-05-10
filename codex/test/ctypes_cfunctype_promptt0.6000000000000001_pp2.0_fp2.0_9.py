import ctypes
# Test ctypes.CFUNCTYPE
def func(x, y, z):
    return x * y * z

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmps = []
for i in range(10):
    cmps.append(CMPFUNC(lambda x, y, z=i: func(x, y, z)))

for f in cmps:
    print(f(2, 3))
# Test ctypes.PYFUNCTYPE
def func(x, y):
    return x * y

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmps = []
for i in range(10):
    cmps.append(CMPFUNC(lambda x, y, z=i: func(x, y)))

for f in cmps:
    print(f(2, 3))
 
# Test ctypes.WINFUNCTYPE
