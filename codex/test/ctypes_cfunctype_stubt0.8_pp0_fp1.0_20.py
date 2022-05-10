import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# Python 2.7
# d = {fun: 42}
# TypeError: unhashable type: 'PyCFunctionObject'
