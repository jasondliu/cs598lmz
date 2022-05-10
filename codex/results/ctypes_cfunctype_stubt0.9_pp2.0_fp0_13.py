import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return "%d" % (12345)

def wrap(lib, name):
    return ctypes.pythonapi.PyCObject_FromVoidPtr(
        lib[name](), None).value

Value = wrap(test, "ReturnValue")
print("Value: %s" % (Value))


print("READY.")
sys.exit(0)
