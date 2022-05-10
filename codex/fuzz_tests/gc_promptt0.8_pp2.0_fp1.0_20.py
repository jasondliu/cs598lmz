import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect.
class A:
    pass
a = A()
b = A()
print "collecting A"
gc.collect()
del a, b
gc.collect()
assert gc.collect() == 0
print "collecting B"
class B:
    pass
b = B()
gc.collect()
del b
gc.collect()
assert gc.collect() == 0
print "collecting C"
class C:
    pass
c = C()
gc.collect()
assert gc.collect() == 1
print "collecting D"
class D:
    pass
d = D()
del d
gc.collect()
assert gc.collect() == 1
print "collecting E"
class E:
    pass
e = E()
x = E()
del e
gc.collect()
assert gc.collect() == 2
print "collecting F"
class F:
    pass
f = F()
y = F()
del f
gc.collect()
assert gc.collect() == 2
print "collecting G"
class G:
    pass
