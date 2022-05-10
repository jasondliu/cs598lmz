import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

result = ctypes.CDLL("./libdll.so", mode = ctypes.RTLD_GLOBAL)

temp = FUNTYPE(result.foo)

# Python has no pointer to int type
# so we need to provide a pointer to a pointer
# and extract the value from the pointer
x = ctypes.pointer(ctypes.c_int(0))
print(temp(x))
print(x.contents.value)
