import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print('1:', gc.collect())
def f(i):
    print(gc.collect(), i)
    if i > 0:
        gc.collect()
f(0)
f(-1)

# Test gc.get_referrers()
a = [1]
b = a
print(gc.get_referrers(a))
del a, b
print(gc.get_referrers(gc.get_referrers))

# Test gc.get_objects()
class A:
    pass
#gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_threshold(1)
del A.__del__
a = A()
b = A()
print(a, b, a.__del__)

class B(A):
    pass
c = B()
d = B()
print(c, d, c.__del__)

class C:
    pass
e = C()
f = C()
print(e, f, e.__del__)
del c,
