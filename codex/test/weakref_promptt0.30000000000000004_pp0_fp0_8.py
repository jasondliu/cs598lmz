import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())
print(r() is a)

del a
print(r())

# Test weakref.proxy()

a = A()
p = weakref.proxy(a)
print(p)
print(p is a)

del a
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

a = A()
print(weakref.getweakrefcount(a))
r1 = weakref.ref(a)
print(weakref.getweakrefcount(a))
r2 = weakref.ref(a)
print(weakref.getweakrefcount(a))
del r1
print(weakref.getweakrefcount(a))
del r2
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()

a = A()
