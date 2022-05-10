import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hi")
    return "hi"

o = fun()
print(o)
</code>

