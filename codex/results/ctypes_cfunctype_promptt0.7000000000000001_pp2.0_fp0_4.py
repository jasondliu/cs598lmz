import ctypes
# Test ctypes.CFUNCTYPE
def py_foo(x, y):
    return x + y

foo = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(py_foo)

print("foo(1,1): %f" % foo(1.0, 1.0))

# Test ctypes.PYFUNCTYPE
def py_foo(x):
    return x


foo = ctypes.PYFUNCTYPE(ctypes.c_double, ctypes.c_double)(py_foo)

print("foo(1): %f" % foo(1.0))

# Test ctypes.WINFUNCTYPE
def py_foo(a, b, c):
    return a + b + c

foo = ctypes.WINFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)(py_foo)

print("foo(1,1,1): %f" % foo(1.0, 1.0
