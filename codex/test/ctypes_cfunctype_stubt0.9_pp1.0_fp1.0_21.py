import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise SystemError
# The following checks that object.__new__(catcher) does not call repr
# on catcher, by passing it a class whose repr raises an exception.
