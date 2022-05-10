import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())

del a
print(r())

# Test weakref.proxy()

class B:
    pass

b = B()
p = weakref.proxy(b)
print(p)
print(p.__class__)

del b
print(p)

# Test weakref.getweakrefcount()

class C:
    pass

c = C()
r1 = weakref.ref(c)
r2 = weakref.ref(c)
r3 = weakref.ref(c)
print(weakref.getweakrefcount(c))

del r1
print(weakref.getweakrefcount(c))

del r2
print(weakref.getweakrefcount(c))

del r3
print(weakref.getweakrefcount(c))

# Test weakref.getweakrefs()

class D:
    pass

d = D()
r1
