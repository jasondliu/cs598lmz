import weakref
# Test weakref.ref()

class Foo:
    pass

a = Foo()
r = weakref.ref(a)
print(r)
print(r())

del a
print(r)
print(r())

# Test weakref.proxy()

class Foo:
    pass

a = Foo()
r = weakref.proxy(a)
print(r)
print(r.__class__)

del a
print(r)
print(r.__class__)

# Test weakref.getweakrefcount()

class Foo:
    pass

a = Foo()
b = Foo()

print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))

r = weakref.ref(a)
print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))

# Test weakref.getweakrefs()

class Foo:
    pass

a = Foo()
b = Foo()

print(weakref.getweakrefs(a))

