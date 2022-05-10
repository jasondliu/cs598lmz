import ctypes
# Test ctypes.CFUNCTYPE
try:
    ctypes.CFUNCTYPE
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test CFUNCTYPE(None)
x = ctypes.CFUNCTYPE(None)(lambda x: x)
print(x)

# Test more complex CFUNCTYPE
x = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p)(lambda x, y, z: x)
print(x)

# Test CFUNCTYPE that throws
def bar(*args):
    raise ValueError

x = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(bar)
print(x)

try:
    x(1, 2)
except ValueError:
    print("ValueError")

# Test different param types
