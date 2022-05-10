fn = lambda: None
# Test fn.__code__
bogusFn.__code__ = '42'
# Test type.__bases__
bogusType = type(None)
bogusType.__bases__ = '42'
# Test metaclass.__call__, metaclass.__new__
bogusMetaclass = type(type)
bogusMetaclass.__call__ = '42'
bogusMetaclass.__new__ = '42'

class C:

    def getattr(self, attr):
        self._attr = attr

    def get__module__(self):
        return self.__module__

    def get__class__(self):
        return self.__class__

    def get__name__(self):
        return self.__name__

    def get__bases__(self):
        return self.__bases__

    def get__mro__(self):
        return self.__mro__

    def get__call__(self):
        return self.__call__

    def get__new__(self):
       
