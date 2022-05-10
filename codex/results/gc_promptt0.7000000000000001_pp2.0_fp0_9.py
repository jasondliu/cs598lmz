import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class Foo(object):
    pass
f = Foo()
foo_id = id(f)
del f
gc.collect()
assert gc.collectable(foo_id)

class Bar(object):
    def __del__(self):
        pass
b = Bar()
bar_id = id(b)
del b
gc.collect()
assert not gc.collectable(bar_id)

assert gc.collectable(42)
# Test gc.get_referrers()
def f():
    return gc.get_referrers(42)

assert f() == [{42: 42}]

def f():
    return gc.get_referrers([])

assert f() == [[]]

def f():
    return gc.get_referrers(f)

assert f() == [{f: f}, {f: f}, {f: f}, {f: f}, {f: f}]

def f():
    return gc.get_referrers({})

assert f() ==
