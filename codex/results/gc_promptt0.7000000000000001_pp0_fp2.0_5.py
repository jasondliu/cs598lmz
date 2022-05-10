import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() vs. gc.garbage
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

for c in [A, B, C, D]:
    for i in range(2):
        x = c()
        x.a = A()
        x.b = B()
        x.c = C()
        x.d = D()
        del x
    gc.collect()
    if gc.garbage:
        print "FAIL", c
        print gc.garbage
    del c
    gc.collect()
    if gc.garbage:
        print "FAIL2", c
        print gc.garbage

# Test gc.get_threshold()
gc.set_debug(gc.DEBUG_STATS)
t = gc.get_threshold()
print t
gc.set_threshold(t)
t2 = gc.get_threshold()
if t != t2:
    print "FAIL", t
