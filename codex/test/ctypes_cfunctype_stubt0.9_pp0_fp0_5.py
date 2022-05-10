import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello world!")

cfun = FUNTYPE(fun)
obj = ctypes.py_object(cfun)
import dis
dis.dis(obj)
print(repr(obj))

# both outputs contain
# CALL_FUNCTION 3 (2 positional, 1 keyword pair)
