import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def f(x):
    return var * x
c_f = FUNTYPE(f)
c_f(0)

assert pointer(x).value == x
# ctypes.sizeof(data1)
import numpy as np
m = np.eye(3)
a = np.arange(3)
b = a.copy()
c = np.dot(m, a)
assert np.all(b == a)
assert not np.all(b == c)
np.dot(np.ones((3,1000,1000)), np.eye(1000))
import numpy as np
import time
t1 = time.time()
a = np.empty((3,1000))
for i in range(3000000):
    c = np.dot(a, a)
t2 = time.time()
print(t2 - t1)
dessert = np.eye(1000)
t1 = time.time()
for i in range(3000000):
    c = np.dot(a, dessert)

