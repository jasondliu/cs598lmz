import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
class E:
    pass
for o in [A, B, C, D, E]:
    o.__module__ = 'm'
    o.__name__ = o.__qualname__ = o.__name__
    o.__qualname__ = 'm.' + o.__name__
    o.__doc__ = 'docstring'
    o.__dict__ = {'__module__': 'm', '__doc__': 'docstring'}
    o.__weakref__ = weakref.ref(o)
    o.__slots__ = ()
    o.__bases__ = ()
    o.__subclasses__ = []
    o.__flags__ = 0
    o.__dictoffset__ = 0
    o.__weaklistoffset__ = 0
    o.__base__ = object
    o.__mro__ = ()
    o.__subclasshook__ = NotImple
