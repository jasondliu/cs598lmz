import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(n):
    print('callback', n)
    return n

f = FUNTYPE(callback)

print(f(1))
</code>

