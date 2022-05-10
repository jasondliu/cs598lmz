import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
pfn = FUNTYPE(f)
pfn(1)

pfn = FUNTYPE(lambda x: x*x)
pfn(2)
 
print(pfn.__class__, type(pfn))
print(pfn.__doc__)

#int __stdcall MyCallback(double x)
#{
#    return x + 1;
#}

pfn.restype = ctypes.c_int
pfn.argtypes = [ctypes.c_double]
print(pfn(3))
