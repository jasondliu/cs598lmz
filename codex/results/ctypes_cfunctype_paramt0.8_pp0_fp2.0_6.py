import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def _print(arg):
    print("hi")
    return ctypes.c_int(arg)

f = FUNTYPE(_print)
print(f(ctypes.c_int(5)))
</code>
If you don't want to use ctypes, you can use <code>ctypes.pythonapi</code> and access functions from the <code>PyCObject_*</code> API:
<code>import ctypes
from ctypes import pythonapi
PyCapsule_CheckExact = pythonapi.PyCapsule_CheckExact
PyCapsule_GetPointer = pythonapi.PyCapsule_GetPointer

def _print(arg):
    print("hi")
    return arg

f = _print
capsule = ctypes.py_object(f)
assert PyCapsule_CheckExact(capsule)
fn = PyCapsule_GetPointer(capsule, None)
print(fn(5))
</code>
A more high-level solution is to use
