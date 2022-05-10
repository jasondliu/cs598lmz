import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B:
    pass

a = A()
b = B()
a.b = b
b.a = a

a_wr = weakref.ref(a)
b_wr = weakref.ref(b)

#print gc.collect()
assert gc.collect() == 0
assert gc.collect() == 0
del a
assert gc.collect() == 1
assert gc.collect() == 0
del b
assert gc.collect() == 1
assert gc.collect() == 0

print 'passed'
