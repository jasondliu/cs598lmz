import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

@ctypes.WINFUNCTYPE(ctypes.wintypes.BOOL, ctypes.c_int)
def fun_c(arg):
    print(arg)
    return True

types.PyType_Ready(fun)
types.PyType_Ready(fun_c)

print(dll.PyType_IsSubtype(fun_c, fun))
print(dll.PyType_IsSubtype(fun, fun_c))
print(dll.PyType_IsSubtype(fun, fun))
</code>
output:
<code>True
False
True
</code>

