import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
def f():
    return None
print(ctypes.cast(f, ctypes.py_object).value is f)
</code>
prints <code>True</code>.

