import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def function(x):
    return x*x
func = FUNTYPE(function)

print func(2.0)

import math
print math.sin(.1)
sin = FUNTYPE(math.sin)
print sin(.1)

print math.cos(.1)
cos = FUNTYPE(math.cos)
print cos(.1)

print math.tan(.1)
print tan(.1)

print math.atan(.1)
print atan(.1)
