import ctypes
# Test ctypes.CFUNCTYPE()
def foo(x):
    print("In foo(), x =", x)

myCFunc = ctypes.CFUNCTYPE(None, ctypes.c_int)(foo)

myCFunc(1)

# Test ctypes.WINFUNCTYPE()
def bar(x, y):
    print("In bar(), x =", x, "y =", y)

