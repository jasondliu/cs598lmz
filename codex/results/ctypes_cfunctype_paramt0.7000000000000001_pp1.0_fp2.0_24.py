import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float, ctypes.c_float)

def f(x, y):
    return x*x + y*y


func_ptr = FUNTYPE(f)

ff = FUNTYPE(lambda x, y: x*x + y*y)

some_func = FUNTYPE(lambda x, y: x*x + y*y)
result = some_func(1, 2)
print(result)

f = lambda x, y: x*x + y*y

res = f(1,2)
print(res)

f = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float, ctypes.c_float)(lambda x, y: x*x + y*y)

res = f(2,3)
print(res)
