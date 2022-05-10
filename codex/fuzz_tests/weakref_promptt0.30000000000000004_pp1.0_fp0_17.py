import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o = 1
print(r())

o = C()
print(r())

del o
print(r())

# Test weakref.getweakrefs(obj)

class C:
    pass

o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
r3 = weakref.ref(o)

print(weakref.getweakrefs(o))

# Test weakref.getweakrefcount(obj)

class C:
    pass

o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
r3 = weakref.ref(o)

print(weakref.getweakrefcount(o))

# Test weakref.proxy(obj)

class C:
    pass

o = C()
p = weakref.proxy(o)
print(
