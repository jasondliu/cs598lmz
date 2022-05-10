import ctypes
# Test ctypes.CFUNCTYPE()
def foo(x):
    print("In foo(), x =", x)

myCFunc = ctypes.CFUNCTYPE(None, ctypes.c_int)(foo)

myCFunc(1)

# Test ctypes.WINFUNCTYPE()
def bar(x, y):
    print("In bar(), x =", x, "y =", y)

myWfunc = ctypes.WINFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(bar)

myWfunc(1, 2)

# Test ctypes.PYFUNCTYPE()
def baz(x, y):
    print("In baz(), x =", x, "y =", y)

myPfunc = ctypes.PYFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(baz)

myPfunc(1, 2)
</code>
The output is:
<code>In foo(), x = 1
In bar(), x = 1 y = 2
In baz
