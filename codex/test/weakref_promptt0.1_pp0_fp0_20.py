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
b = A()

print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))

r = weakref.ref(a)
print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))

p = weakref.proxy(a)
print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))

# Test weakref.getweakrefs()

a = A()
b = A()


