import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    """Ha ha ha, I'm a useless callback!"""
    return True


