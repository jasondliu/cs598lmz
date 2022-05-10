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

class B:
    pass

b = B()
p = weakref.proxy(b)
print(p)
print(p.__class__)

del b
print(p)
print(p.__class__)

# Test weakref.getweakrefcount()

class C:
    pass

c = C()
print(weakref.getweakrefcount(c))

r = weakref.ref(c)
print(weakref.getweakrefcount(c))

p = weakref.proxy(c)
print(weakref.getweakrefcount(c))

# Test weakref.getweakrefs()

class D:
    pass

d = D()
print(weakref.getweakrefs(d))

r = weakref.ref(d)
