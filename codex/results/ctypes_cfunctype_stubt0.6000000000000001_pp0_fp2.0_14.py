import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "42"

@fun.register(int)
def fun_int(arg):
    return int(arg)

print(fun())
print(fun(42))
</code>
<code>42
42
</code>

