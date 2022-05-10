import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2():
    return "hello"

print(fun())
print(fun2())
</code>
Output:
<code>hello
hello
</code>

