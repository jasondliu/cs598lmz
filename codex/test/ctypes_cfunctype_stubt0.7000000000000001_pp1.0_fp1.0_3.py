import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

class Fun:
    __slots__ = ('__func', '__name')
    def __init__(self, func):
        self.__func = func
        self.__name = func.__name__
    def __call__(self, *args, **kwargs):
        return self.__func(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return types.MethodType(self, instance)

    def __repr__(self):
        return '<fun %s at 0x%x>' % (self.__name, id(self))

    def __str__(self):
        return self.__name

def Method(func):
    return Fun(func)

def main():
    f = fun
    print(repr(f), type(f), len(f))
    f()
    print(repr(fun), type(fun), len(fun))
    fun()

    m = Method(lambda self:print('Method', self))
