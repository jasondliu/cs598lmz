import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())

del a
print(r)
print(r())

# Test weakref.proxy()

a = A()
p = weakref.proxy(a)
print(p)
print(p.__class__)

del a
print(p)
print(p.__class__)

# Test weakref.getweakrefcount()

a = A()
print(weakref.getweakrefcount(a))

r = weakref.ref(a)
print(weakref.getweakrefcount(a))

p = weakref.proxy(a)
print(weakref.getweakrefcount(a))

del r
print(weakref.getweakrefcount(a))

del p
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()

a = A()
print(weakref.getweakrefs(a))

r = weak
