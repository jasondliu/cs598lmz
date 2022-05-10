import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
# CTypes includes a module __builtin__, just like CPython.
# But you have to set the name of the module properly.
# In this case, that module is called funmodule.
