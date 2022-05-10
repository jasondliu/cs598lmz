import weakref

def _isclass(a):
    return isinstance(a, type(type))

class classproperty(object):
    def __init__(self,fget,fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self,owner_self,owner_cls):
        return self.fget(owner_cls)

    def __set__(self,owner_self,value):
        if not self.fset:
            raise AttributeError("can't set attribute")
        self.fset(owner_self,value)

    def setter(self,fset):
        return self.__class__(self.fget,fset)

def classproperty_optimized_decorator(fget):
    if not callable(fget):
        raise TypeError('@classproperty: setter must be callable')
    fset = fget.__set__
    if fset is not None:
        raise TypeError('@classproperty: setter defined but not called')
    return
