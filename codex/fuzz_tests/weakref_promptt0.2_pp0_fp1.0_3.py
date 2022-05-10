import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())

print(r is r2)
print(r() is r2())

print(r() is o)
print(r2() is o2)

# Test weakref.proxy()

p = weakref.proxy(o)
print(p)
print(p is o)
print(p is r())

print(p is o2)
print(p is r2())

# Test weakref.getweakrefcount()

print(weakref.getweakrefcount(o))
print(weakref.getweakrefcount(o2))
print(weakref.getweakrefcount(r()))
print(weakref.getweakrefcount(r2()))

# Test weakref.getweakrefs()

print(weakref.getweakrefs(o))

