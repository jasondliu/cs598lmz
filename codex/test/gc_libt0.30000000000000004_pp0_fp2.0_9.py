import gc, weakref

class A:
    pass

a = A()
a.b = A()
a.b.a = a

print(gc.get_referrers(a))
print(gc.get_referrers(a.b))
print(gc.get_referrers(a.b.a))

print(gc.get_referents(a))
print(gc.get_referents(a.b))
print(gc.get_referents(a.b.a))

print(gc.get_referrers(a)[0])
print(gc.get_referrers(a.b)[0])
print(gc.get_referrers(a.b.a)[0])

