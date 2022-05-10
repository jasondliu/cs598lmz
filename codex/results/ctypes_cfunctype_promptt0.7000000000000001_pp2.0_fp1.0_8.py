import ctypes
# Test ctypes.CFUNCTYPE()

def C(x):
    return x+1

# ref: https://docs.python.org/2/library/ctypes.html#callback-functions
C = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(C)

print C(2)


# Test np.vectorize()
import numpy as np
vC = np.vectorize(C)

print vC([1,2,3])


# Test np.frompyfunc()
def C(x):
    return x+1

fC = np.frompyfunc(C, 1, 1)

print fC([1,2,3])

# Test map
print map(C, [1,2,3])
