import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f = FUNTYPE(lambda x: x * x)
print f(5)
# 25
</code>

