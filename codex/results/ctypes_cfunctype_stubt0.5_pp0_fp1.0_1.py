import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# OK
print(fun())

# OK
print(fun)

# OK
print(fun(1))

# OK
print(fun(1, 2))

# OK
print(fun(1, 2, 3))
</code>
I am not sure what is the actual problem.

