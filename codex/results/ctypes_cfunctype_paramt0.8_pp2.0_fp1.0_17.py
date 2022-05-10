import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
f = FUNTYPE(cdll.testlib.f)
print(f(1.0))
</code>

