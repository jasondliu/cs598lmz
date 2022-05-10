import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return sys.modules[fun.__module__]


# Do it again, using a different name
class mod:
    pass
mod = mod()
mod.fun = FUNTYPE(fun)

