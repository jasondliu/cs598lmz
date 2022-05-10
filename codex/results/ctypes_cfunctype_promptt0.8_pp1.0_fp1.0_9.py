import ctypes
# Test ctypes.CFUNCTYPE

try:
    from ctypes import CFUNCTYPE
except (ImportError, AttributeError):
    import sys
    print("SKIP")
    sys.exit()


functype = CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@functype
def double(i):
    return i * 2

@functype(ctypes.c_float, ctypes.c_int)
def twice(i):
    return i * 2.0

print(double(2))
print(twice(2))
