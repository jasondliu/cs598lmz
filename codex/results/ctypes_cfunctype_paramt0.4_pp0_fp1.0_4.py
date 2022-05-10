import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

f = FUNTYPE(func)
print(f(1))

# Callback function
def callback(x):
    print(x)

f = FUNTYPE(callback)
f(1)

# Callback function with arguments
def callback(x, y):
    print(x + y)

f = FUNTYPE(callback, argtypes=[ctypes.c_int, ctypes.c_int])
f(1, 2)

# Callback function with arguments and return value
def callback(x, y):
    return x + y

f = FUNTYPE(callback, argtypes=[ctypes.c_int, ctypes.c_int], restype=ctypes.c_int)
print(f(1, 2))
