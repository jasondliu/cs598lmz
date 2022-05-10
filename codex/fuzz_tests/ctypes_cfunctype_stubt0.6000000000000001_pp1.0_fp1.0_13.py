import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello World")
    return None

print(type(fun))
print(type(fun()))
print(type(fun.__call__()))
</code>
prints
<code>&lt;class 'builtin_function_or_method'&gt;
None
None
</code>

