import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello World")
    return 42

print(fun())
</code>
Output:
<code>Hello World
42
</code>

