import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hi'

print(fun()) # prints 'hi'

# The following works, too.
class C(ctypes.Structure):
    _fields_ = [('fun', FUNTYPE)]
