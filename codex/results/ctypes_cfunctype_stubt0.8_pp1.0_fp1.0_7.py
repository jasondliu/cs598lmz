import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 22

print(fun())
print(fun() is None)
</code>
Once <code>fun</code> is called, it'll return <code>None</code> until Python's GC destroys it. You probably want to make your function return a <code>Py_INCREF</code>ed reference to that object:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object(22)

print(fun())
print(fun() is None)
</code>
Output:
<code>22
False
</code>

