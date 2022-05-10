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
try:
    exec "n.foo = 3"
    raise TestFailed, "__setattr__ not called on __dict__ access"
except AttributeError:
    pass
n.foobar = 4
n.__dict__

class C(object):
    __slots__ = ['foo', '__bar', '__dict__']
    def __init__(self):
        self.foo = 1

c = C()
c.foo = 2
c.bar = 3
c.__dict__
dir(c)

# Generated names
