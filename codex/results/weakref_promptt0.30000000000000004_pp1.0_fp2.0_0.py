import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
del o
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)
print(p is o)
del o
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

o = C()
print(weakref.getweakrefcount(o))
r1 = weakref.ref(o)
print(weakref.getweakrefcount(o))
r2 = weakref.ref(o)
print(weakref.getweakrefcount(o))
del r1
print(weakref.getweakrefcount(o))
del r2
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

o = C()
print(weakref.getweakrefs(o
