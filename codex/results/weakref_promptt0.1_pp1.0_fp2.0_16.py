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

class A:
    pass

a = A()
p = weakref.proxy(a)
print(p)
print(p.__class__)

del a
print(p)

# Test weakref.getweakrefcount()

class A:
    pass

a = A()
r = weakref.ref(a)
print(weakref.getweakrefcount(a))

del a
print(weakref.getweakrefcount(r))

# Test weakref.getweakrefs()

class A:
    pass

a = A()
r = weakref.ref(a)
print(weakref.getweakrefs(a))

del a
print(weakref.getweakrefs(r))

# Test weakref.finalize()

class A:
    pass

a = A
