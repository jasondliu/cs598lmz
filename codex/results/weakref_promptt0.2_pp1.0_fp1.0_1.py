import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())
print(r() is a)

# Test weakref.proxy()

class B:
    pass

b = B()
p = weakref.proxy(b)
print(p)
print(p is b)

# Test weakref.getweakrefcount()

class C:
    pass

c1 = C()
c2 = C()

w1 = weakref.ref(c1)
w2 = weakref.ref(c1)
w3 = weakref.ref(c2)

print(weakref.getweakrefcount(c1))
print(weakref.getweakrefcount(c2))

# Test weakref.getweakrefs()

print(weakref.getweakrefs(c1))
print(weakref.getweakrefs(c2))

# Test weakref.WeakKeyDictionary

class D:
    pass

d1 = D()

