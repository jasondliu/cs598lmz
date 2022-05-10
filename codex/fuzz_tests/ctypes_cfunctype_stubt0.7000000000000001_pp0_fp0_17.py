import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise ValueError

def f(x):
    if x:
        return fun
    else:
        return lambda: None

f(True)()
f(False)()
</code>

