import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
fun = FUNTYPE(lambda: print("hello"))
fun()

print("ADD:")
ADDTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
add_fun = ADDTYPE(lambda x, y: x + y)
result = add_fun(4, 5)
print(result)
