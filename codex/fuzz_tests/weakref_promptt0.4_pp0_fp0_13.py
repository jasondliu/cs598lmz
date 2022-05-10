import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r)
print(r())

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)
print(p.foo)

del o
print(p)
print(p.foo)

# Test weakref.getweakrefcount()

class C:
    pass

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

p = weakref.proxy(o)
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

class C:
    pass

o = C()
print(weakref.getweakrefs(o))

r = weakref.ref(o)
print(weakref.getweak
