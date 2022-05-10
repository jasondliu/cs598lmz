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

o = C()
p = weakref.proxy(o)
print(p)

del o
print(p)

# Test weakref.getweakrefcount()

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

p = weakref.proxy(o)
print(weakref.getweakrefcount(o))

del r
print(weakref.getweakrefcount(o))

del p
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

o = C()
print(weakref.getweakrefs(o))

r = weakref.ref(o)
print(weakref.getweakrefs(o
