import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello\n"
strtype = type("")
if isinstance("", strtype):
    print("instance")
print("fun is", repr(fun))
print("fun() is", repr(fun()))
