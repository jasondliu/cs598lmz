import ctypes
# Test ctypes.CFUNCTYPE
prototype = ctypes.CFUNCTYPE(ctypes.c_long)
def py_fn(arg):
    return arg * 5
c_fn = prototype(py_fn)
print(c_fn(42))
print('#' * 23 + 'Its a C function that can be used from C, and from Python')

import math
# Prototype: double cos(double)
c_cos = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)(math.cos)
print(c_cos(2.0))
print(math.cos(2.0))

# Prototype: double cos(double)
c_sin = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)(math.sin)
print(c_sin(2.0))
print(math.sin(2.0))
print('#' * 23 + 'The point isnt to hide everything behind a nice Python API')

print('#' * 23 + 'Create C callback functions that can be called from C')

prototype =
