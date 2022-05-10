import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
l = []

class A:
    pass
def f(x):
    l.append(x)
# make some cyclic references
a = A()
a.x = a
b = A()
b.x = b
c = A()
c.x = c
# make a list of objects
l = [A(), a, A(), b, A(), c]
# create more cyclic references
a.x = [a, b, c]
b.x = [b, c, a]
c.x = [c, a, b]
# register a callback for a
wr = weakref.ref(a, f)
# create a reference cycle
a.x = [a]
b.x = [b]
c.x = [c]
# break the cycle
a.x = A()
b.x = A()
c.x = A()
# check that the callback was called
assert l == [a], l
# check that the objects were collected
assert wr() is None, wr()
assert wr() is None, wr()
assert wr() is
