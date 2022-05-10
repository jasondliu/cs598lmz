import types
types.MethodType(lambda self: None, None, Dummy)

# __dict__ assignment
class Dictless(object):
    __slots__ = ['a']

Dictless.__dict__ = types.MappingProxyType({'b': 1})
Dictless.__dict__

# __weakref__ assignment
class Foo(object):
    pass

f = Foo()
f.__weakref__ = 42

# __annotations__ assignment
class Foo:
    pass

Foo.__annotations__ = 42

# __class__ assignment
class Foo:
    pass

f = Foo()
f.__class__ = 42

# __bases__ assignment
