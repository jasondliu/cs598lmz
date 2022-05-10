from types import FunctionType
list(FunctionType(x,globals()).__globals__.keys())

list(FunctionType(x,globals()).__globals__.values())
class F:
    def __init__(self,a):
        self.val = a
    def __call__(self,b):
        self.val *= b
        return self.val
f = F(2)
f(10)
f(10)
y = FunctionType(x,globals())
y
y.__globals__ is globals()
y.__globals__ is dir()
y.__globals__ is y.__closure__
dir()
y.__closure__ is dir()
dir()
dir().keys()
dir().values()
dir() is globals()
dir() is globals().keys()
dir() is globals().values()
dir() == globals()
dir() == globals().keys()
dir() == globals().values()
globals().keys()
globals().values()
list(globals().keys())
list(glob
