import weakref
# Test weakref.ref()

class Foo:
    pass

a = Foo()
r = weakref.ref(a)
print(r)
print(r())
print(r() is a)

print(r() is None)
del a
print(r() is None)

# Test weakref.proxy()

class Foo:
    pass

a = Foo()
r = weakref.proxy(a)
print(r)
print(r is a)

print(r is None)
del a
print(r is None)

# Test weakref.getweakrefcount()

class Foo:
    pass

a = Foo()
r = weakref.ref(a)
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()

class Foo:
    pass

a = Foo()
r = weakref.ref(a)
print(weakref.getweakrefs(a))

# Test weakref.WeakKeyDictionary()

class Foo:
    pass

a = Foo()
d = weakref
