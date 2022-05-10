import ctypes
# Test ctypes.CFUNCTYPE on a generic function
def func(x, y):
    if x != y:
        raise ValueError
    return x
