import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise ValueError("Test")

try:
    junk = fun()
except ValueError as e:
    print("Got expected exception", e)
else:
    print("Unexpectedly got no exception")
