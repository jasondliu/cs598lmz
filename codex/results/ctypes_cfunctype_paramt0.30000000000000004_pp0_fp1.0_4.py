import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(n):
    print("callback called with", n)
    return n * 2

cb = FUNTYPE(callback)

lib.call_callback(cb, 5)

# Output:
# callback called with 5
# 10
</code>

