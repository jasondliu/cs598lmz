import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect method of weakref.ReferenceType
class Bar:
    def __del__(self):
        return 42
b = Bar()
x = weakref.ref(b)
print x(), 1, len(gc.get_objects())
print x() is b
print x() is b, 2, len(gc.get_objects())
del b
gc.collect()
#print x() is... AttributeError: __del__ attribute should have raised 42
print x(), 3, len(gc.get_objects())
# test a bug in get_referrers
class Foo:
    def foo(object):
        pass
a = []
a.append(weakref.ref(a))
print len(gc.get_referrers(a))
f = Foo()
g = type.__call__(type(f),f)
#print len(gc.get_referrers(f))
print len(gc.get_referrers(g))
# test the counts returned by get_count()
class FooBase:
    def __init__(self,*args,**kw):
        self
