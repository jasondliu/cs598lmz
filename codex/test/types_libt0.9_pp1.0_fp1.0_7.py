import types
types.MethodType(add, None, Foo)
types.MethodType(add, Foo, Foo)


class NoSetattr(Foo):
    __slots__ = []
    def __setattr__(self, attr, value):
        raise AttributeError

hasattr(NoSetattr, '__dict__')
hasattr(NoSetattr, '__setattr__')
getattr(NoSetattr, '__setattr__')
dir(NoSetattr)

n = NoSetattr()
n.__dict__
