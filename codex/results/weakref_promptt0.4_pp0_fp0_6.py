import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)

print(r())

print(r() is a)

print(r() is None)

a = None
print(r() is None)

# Test weakref.proxy()
a = A()
p = weakref.proxy(a)
print(p)

print(p is a)

print(p.__class__)

a = None
print(p is None)

# Test weakref.getweakrefcount()
a = A()
print(weakref.getweakrefcount(a))

b = weakref.ref(a)
print(weakref.getweakrefcount(a))

c = weakref.proxy(a)
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()
a = A()
print(weakref.getweakrefs(a))

b = weakref.ref(a)
print(weakref.getweakrefs
