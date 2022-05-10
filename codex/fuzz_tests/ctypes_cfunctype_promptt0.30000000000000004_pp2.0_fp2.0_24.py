import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print("callback called with", x)
    return x

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

lib = ctypes.CDLL("./libtest.so")
lib.test_callback.argtypes = (CALLBACK, ctypes.c_int)
lib.test_callback.restype = ctypes.c_int

print(lib.test_callback(CALLBACK(callback), 42))
</code>
This prints
<code>callback called with 42
42
</code>

