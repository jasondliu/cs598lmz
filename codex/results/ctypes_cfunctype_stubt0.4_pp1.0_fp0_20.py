import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return "world"

print(fun())
</code>
prints
<code>hello
world
</code>

