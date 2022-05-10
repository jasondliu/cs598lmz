import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    print("hello from Python")
    return n + 42

CALLBACK = FUNTYPE(func)

lib.call_me_back(CALLBACK)
</code>

