import weakref
# Test weakref.ref()
class C:
    pass

o = C()
r = weakref.ref(o)
print(r())
print(bool(r))
print(r is not None)
print(r() is o)

print(r() is None)
print(bool(r))
print(r is not None)

r = weakref.ref(o)
r() is o
r() is o
r() is o
r() is o

# Test weakref.proxy
o = C()
p = weakref.proxy(o)
print(p.__class__)
print(type(p))

# Test weakref.getweakrefcount()
o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
r3 = weakref.ref(o)
print(weakref.getweakrefcount(o))
print(weakref.getweakrefcount(o) == 3)

# Test weakref.getweakrefs()
o = C()
r1 = weakref.ref(o)
r
