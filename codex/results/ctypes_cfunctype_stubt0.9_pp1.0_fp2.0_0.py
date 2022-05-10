import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    x = "Hello"
    x *= 3
    return x

print(cast(fun, _voidpp).contents.value)
x = cast(_voidpp, _double)
print(fun(), x)
assert(x[0] == 0)
y = cast(_doubl
