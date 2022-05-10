import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

f = fun()
</code>
Note that although I did declare the return type of the <code>CFUNCTYPE</code> as <code>py_object</code>, the <code>FUNTYPE</code> variable itself is of type <code>CFUNCTYPE</code> but not <code>py_object</code>.

