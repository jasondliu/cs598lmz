import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(ctypes.cast(fun, ctypes.c_void_p).value)
print(hex(id(fun)))
print(hex(id(fun.__call__)))
print(ctypes.cast(fun.__call__, ctypes.c_void_p).value)

# fun is a function pointer
# fun.__call__ is a callable object, which calls fun
c_fun = ctypes.cast(fun, FUNTYPE)
print(c_fun)
print(c_fun())
</code>
prints
<code>140252723227680
0x10400f838
0x10400f8d0
140252723227680
&lt;CFUNCTYPE(pyobject) object at 0x10400f838&gt;
hello
</code>
<code>140252723227680</code> is the address of the <code>fun</code> object, <code>0x10400f838</code> is the ID of <code>fun</code> and <code
