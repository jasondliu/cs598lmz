import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

class D:
    pass

o = D()
p = D()
r = weakref.ref(o)
print(r)
print(r())

o = p
print(r())

del p
print(r())

del o
print(r())
