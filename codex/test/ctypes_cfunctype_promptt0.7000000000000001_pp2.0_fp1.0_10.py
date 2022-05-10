import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    print("func")
    return a + b

# Callable prototype: int(int, int)
