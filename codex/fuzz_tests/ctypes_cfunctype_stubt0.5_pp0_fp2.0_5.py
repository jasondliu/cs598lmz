import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello, world!")
    return "Hello, world!"

print(fun())
</code>
Output:
<code>Hello, world!
Hello, world!
</code>

