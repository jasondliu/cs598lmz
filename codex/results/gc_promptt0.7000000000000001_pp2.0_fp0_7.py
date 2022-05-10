import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
def f():
    print 'called'

class Test:
    pass

t1 = Test()
t1.f = f
r1 = weakref.ref(t1)
r1()

del t1
gc.collect()

t2 = Test()
t2.f = f
r2 = weakref.ref(t2)
r2()

del t2
gc.collect()

assert r1() is None
assert r2() is None

print "OK"
