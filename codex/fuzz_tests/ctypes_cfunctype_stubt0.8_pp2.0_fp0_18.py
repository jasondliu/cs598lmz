import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
# CTypes includes a module __builtin__, just like CPython.
# But you have to set the name of the module properly.
# In this case, that module is called funmodule.
__builtin__.__dict__['funmodule'] = ctypes.pythonapi
ctypes.pythonapi.PyCFunction_NewEx.restype = ctypes.py_object
ctypes.pythonapi.PyCFunction_NewEx.argtypes = (ctypes.py_object,
                                               ctypes.py_object,
                                               ctypes.py_object)
__builtin__.__dict__['hello'] = ctypes.pythonapi.PyCFunction_NewEx(ctypes.py_object(fun),
                                                                   ctypes.py_object(None),
                                                                   ctypes.py_object(funmodule))

del __builtin__, ctypes, FUNTYPE, fun
</code>
This code deletes the names that contained ctypes, so we can restore the original (broken) ctypes module, in case we need it.
You can
