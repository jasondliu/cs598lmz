import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print("Callback called with argument:", x)
    return x * 2

CALLBACK = FUNTYPE(callback)

def main():
    lib = ctypes.CDLL("libfoo.so")
    lib.foo(CALLBACK)
</code>

