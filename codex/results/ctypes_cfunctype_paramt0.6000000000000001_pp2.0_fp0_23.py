import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

print(func(1, 2))

func_addr = ctypes.cast(func, ctypes.c_void_p).value
print(func_addr)

test_dll = ctypes.CDLL('./test_dll.so')
func_addr_dll = test_dll.func_addr
print(func_addr_dll)

f = FUNTYPE(func_addr)
print(f(1, 2))

f = FUNTYPE(func_addr_dll)
print(f(1, 2))
