import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
assert fun() == "hello"

print fun()
</code>
which seems to do the trick. So have a look into the sources of <code>ctypes</code>.

