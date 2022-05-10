import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
print(FUNTYPE)
print(type(FUNTYPE))
del FUNTYPE

print(ctypes.c_int)
i = ctypes.c_int(-1)
print(i.value)
print(type(i.value))
print(i)
print(type(i))
ctypes.memset(ctypes.byref(i),0,ctypes.sizeof(i))
print(i.value)
print(type(i.value))
print(i)
print(type(i))
