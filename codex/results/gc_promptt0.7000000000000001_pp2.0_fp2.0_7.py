import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
for i in range(1, 5):
    gc.collect()
    print(gc.garbage)
    gc.garbage = []

# Test gc.get_objects() and gc.get_referrers()
class A:
    pass
a = A()
print(gc.get_referrers(a))
print(gc.get_referrers(A))
print(gc.get_referrers(gc))

refs = gc.get_referrers(gc.get_objects())
#for r in refs:
#    print(r)

# Test weakref.WeakKeyDictionary
class B:
    pass
b1 = B()
b2 = B()
b3 = B()
b4 = B()
b5 = B()
b6 = B()
b7 = B()
b8 = B()
b9 = B()
b10 = B()
b11 = B()
b12 = B()
b13 = B()
b14 = B()
b15 = B()
b16 =
