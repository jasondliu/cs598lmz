import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun.argtypes)
print(fun.restype)
print(fun())
</code>
Output:
<code>()
&lt;class 'object'&gt;
hello
</code>

