from types import FunctionType
a = (x for x in [1])
print(a)
class MagicFunction(FunctionType):
    def __init__(self,func,magic=True):
        self.func = func
        self.magic = magic
    def __call__(self, *args, **kwargs):
        if self.magic:
            print('Magic Happens')
        return self.func(*args, **kwargs)
    
    
def double(x):
    return x*2

double = MagicFunction(double)
print(double(2))

class MagicProperty:
    def __init__(self,fget,fset,fdel):
        pass
    
#magic_property.__get__(obj,type=None)
