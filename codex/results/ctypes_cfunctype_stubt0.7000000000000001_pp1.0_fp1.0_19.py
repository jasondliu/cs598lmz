import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise ValueError

def callback(arg):
    print arg

c_fun = FUNTYPE(fun)

# This should raise a SystemError when called from C
print c_fun()

# This should raise a TypeError when called from C
print fun(callback)

# This should raise a ValueError when called from C
print fun(1)

# This should raise a ValueError when called from C
print fun(1, 2)

# This should raise a ValueError when called from C
print fun(1, 2, 3)

# This should raise a ValueError when called from C
print fun(1, 2, 3, 4)

# This should raise a ValueError when called from C
print fun(1, 2, 3, 4, 5)

# This should raise a ValueError when called from C
print fun(1, 2, 3, 4, 5, 6)

# This should raise a ValueError when called from C
print fun(1, 2, 3, 4, 5, 6, 7)

# This should raise a ValueError when called from C
print fun
