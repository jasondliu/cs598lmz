import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect (if it works)
a = gc.collect()
assert a == 0
# Try it with a Python object
class Foo:
    pass
f = Foo()
f = None
gc.collect()
# Try it with a C object
# (This is not a very good test, but it's better than nothing.)
class Foo:
    pass
def callback(o):
    assert isinstance(o, Foo)
f = Foo()
f = weakref.ref(f, callback)
del f
gc.collect()
# Try it with a weaklist
class Foo:
    pass
f = Foo()
l = weakref.WeakList()
l.append(f)
assert f in l
f = None
gc.collect()
assert len(l) == 0
# Try it with one object depending on another
class Foo:
    pass
f = Foo()
t = (f,)
f = None
gc.collect()
assert len(t) == 0
# Try it with a cycle
class Foo:
    pass
f = Foo()
f.x = f
f = None
gc
