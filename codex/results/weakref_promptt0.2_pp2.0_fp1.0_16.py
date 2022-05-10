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

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p)
print(p.__class__)

del o
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)

print(weakref.getweakrefcount(o))

del o
print(weakref.getweakrefcount(r1))

# Test weakref.getweakrefs()

o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)

print(weakref.getweakrefs(o))

del o
print(weakref.getweakrefs(r1))

