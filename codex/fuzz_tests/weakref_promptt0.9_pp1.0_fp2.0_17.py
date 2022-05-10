import weakref
# Test weakref.ref() in both its types
try:
    # Python 2.x
    class ThisThing(object):
        pass
except NameError:
    # Python 3.x
    ThisThing = object
for typ in (type, ThisThing):
    r = weakref.ref(typ)
    assert r() is typ
# Test weakref.ref() with a keyword argument (issue #14896)
class Type:
    pass

rweakref = weakref.ref(Type, Type)
assert rweakref() is Type
