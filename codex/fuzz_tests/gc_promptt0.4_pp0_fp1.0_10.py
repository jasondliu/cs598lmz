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

a = A()
b = B()
c = C()
d = D()

for o in gc.get_objects():
    if isinstance(o, D):
        print "found a D:", o
        break
else:
    print "no D found"

print "collecting"
n = gc.collect()
print "unreachable objects:", n
print "collecting again"
n = gc.collect()
print "unreachable objects:", n

print "creating cycles"
l = [a, b, c, d]
a.x = l
b.x = l
c.x = l
d.x = l
del l

print "collecting"
n = gc.collect()
print "unreachable objects:", n
print "collecting again"
n = gc.collect()
print "unreachable objects:", n
