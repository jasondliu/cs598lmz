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

class B:
    pass

b = B()
p = weakref.proxy(b)
print(p)
print(p is b)

del b
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

class C:
    pass

c = C()
print(weakref.getweakrefcount(c))

r1 = weakref.ref(c)
print(weakref.getweakrefcount(c))

r2 = weakref.ref(c)
print(weakref.getweakrefcount(c))

del r1
print(weakref.getweakrefcount(c))

del r2
print(weakref.getweakrefcount(c))

# Test weakref.get
