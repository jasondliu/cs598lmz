import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(2)
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

for c in A, B, C, D:
    print gc.is_tracked(c),
print

x = D()
print gc.is_tracked(x),
print

# Create a reference cycle
x.a = x
print gc.is_tracked(x),
print
print gc.get_referrers(x)

# Break the reference cycle
x.a = None
print gc.is_tracked(x),
print

# Track a subclass instance
def setstate(self, state):
    self.__dict__ = state

D.__setstate__ = setstate
t = ([1] * 10, {}, [])
x.__setstate__(t)
print gc.is_tracked(t[0]),
print gc.is_tracked(t[1]),
print gc.is_tracked(t
