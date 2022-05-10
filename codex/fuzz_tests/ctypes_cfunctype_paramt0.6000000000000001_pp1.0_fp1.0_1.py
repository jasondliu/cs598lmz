import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

class PyCFunction:
    def __init__(self,func,name=None):
        self.func = func
        self.name = name or func.__name__
        self.cfunc = FUNTYPE(func)
    
    def __call__(self,*args):
        return self.func(*args)
    
    def __repr__(self):
        return "<PyCFunction %s>" % self.name


class PyCFunctionType:
    def __init__(self,name):
        self.name = name

    def __call__(self,func):
        return PyCFunction(func,name=self.name)


cfunc = PyCFunctionType

@cfunc("sqr")
def square(x):
    return x*x



#print(square(5))

#print(square.cfunc(5))

#print(square.cfunc)

#print(square.cfunc.argtypes)
#print(square.cfunc.restype
