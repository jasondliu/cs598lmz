import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1,2,3]

arr = fun()
print(arr)
</code>
Result:
<code>[1, 2, 3]
</code>

