import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    """Callback type for use with test_callback()"""
    print("Calling fun()")

def test_callback():
    """
    Calling and C callback from Python.
    »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
    • Portability: Pure function.
    • Functions:   ctypes.CFUNCTYPE(ctypes.py_object)
                   ctypes.py_object
    • Types:       None
    """
    cfun = FUNTYPE(fun)
    fptr = ctypes.callbacks.CFUNCTYPE(ctypes.py_object)(cfun)
    fptr()
