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

for c in [A, B, C, D, E]:
    a = c()
    a = None
    gc.collect()
    print gc.collect()

# Test gc.get_objects()

class G:
    pass

a = G()
l = [G(), G()]
d = {'a':G(), 'b':G()}
t = (G(), G(), G())
s = 'abc'

gc.collect()

assert a in gc.get_objects()
for e in l:
    assert e in gc.get_objects()
for e in d.values():
    assert e in gc.get_objects()
for e in t:
    assert e in gc.get_objects()
assert s in gc.get_objects()

# Test gc.get_referrers()

