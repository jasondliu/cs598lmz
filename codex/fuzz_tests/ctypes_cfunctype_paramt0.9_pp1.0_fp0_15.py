import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.py_object)
def CFUNC(fun):
    fun.CALLBACK = FUNTYPE(fun)
    return fun.CALLBACK
    
    
class Point(ctypes.Structure):
    _fields_ = [("x",ctypes.c_double),("y",ctypes.c_double)] 
    def __init__(self,*args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        else:
            raise Exception


class Color(ctypes.Structure):
    _fields_ = [("r",ctypes.c_double),
                ("g",ctypes.c_double),
                ("b",ctypes.c_double),
                ("a",ctypes.c_double)]    
    def __init__(self,*args):
        if len(args) == 4:
            self.r = args[0]
            self.g = args[1]
            self.b = args[2]
            self.a = args[
