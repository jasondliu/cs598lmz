import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)

class FunObj(object):
    def __init__(self, name, fun):
        self.name = name
        self.fun = fun
    def __str__(self):
        return self.name

def fun_obj(name):
    def _(fun):
        return FunObj(name, fun)
    return _

def fun_ptr(fun):
    return FUNTYPE(fun)

@fun_obj("GL_FUNC_ADD")
def GL_FUNC_ADD():
    return 0x8006

@fun_obj("GL_FUNC_SUBTRACT")
def GL_FUNC_SUBTRACT():
    return 0x800a

@fun_obj("GL_FUNC_REVERSE_SUBTRACT")
def GL_FUNC_REVERSE_SUBTRACT():
    return 0x800b

@fun_obj("GL_MIN")
def GL_MIN():
    return
