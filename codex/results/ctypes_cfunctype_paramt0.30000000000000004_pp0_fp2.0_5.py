import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(n):
    print("callback called with", n)
    return n + 1

f = FUNTYPE(callback)

print(f(3))

# callback called with 3
# 4
</code>

