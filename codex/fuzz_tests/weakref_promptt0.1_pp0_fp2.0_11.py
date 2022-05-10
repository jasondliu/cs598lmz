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
# print(p)

# Test weakref.getweakrefcount()

class C:
    pass

c = C()
d = C()

print(weakref.getweakrefcount(c))
print(weakref.getweakrefcount(d))

# Test weakref.getweakrefs()

class D:
    pass

d = D()
e = D()

print(weakref.getweakrefs(d))
print(weakref.getweakrefs(e))

# Test weakref.WeakKeyDictionary()

class E:
    pass

e = E()
f = E()

wkd = weakref
