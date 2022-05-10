import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("called!")
    return 42

print("Got the function %r and result %d!" % (fun, fun()))
