import types
types.MethodType(lambda self, *args, **kwargs: self.__class__.__bases__[0].__init__(self, *args, **kwargs), None, MyClass)
</code>

