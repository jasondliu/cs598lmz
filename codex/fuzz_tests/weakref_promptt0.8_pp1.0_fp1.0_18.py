import weakref
# Test weakref.ref() with a cyclic container and a clear().
import _weakref

class MyList(list):
    pass

a = MyList([1])
b = MyList([2])
a.append(b)
b.append(a)

r = weakref.ref(a)
r2 = weakref.ref(b)

assert callback is None
called = False
def callback(*args):
    global called
    called = True
    assert callback.wr is r
    assert callback.args == args
callback.wr = r
callback.args = (1, 2)

assert not a
assert not b
w = _weakref.ref(a, callback)

assert a
assert b

assert w() is a
assert not called
assert len(_weakref.getweakrefs(a)) == 2
del a, b
assert called
assert not w()
assert w() is None

# This is the same as above except with a global list instead of a
# local.  When the function containing the weakref callback is
# destroyed, the callback must be removed from the global list
