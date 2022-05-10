import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

s = fun()
print(s)
</code>
The output is:
<code>hello
</code>

