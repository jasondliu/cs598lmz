import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(r)
print(r())

del f
print(r)
print(r())

# Test weakref.proxy()

class Foo:
    pass

f = Foo()
p = weakref.proxy(f)
print(p)
print(p.__class__)

del f
print(p)
print(p.__class__)

# Test weakref.getweakrefcount()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(weakref.getweakrefcount(f))

# Test weakref.getweakrefs()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(weakref.getweakrefs(f))

# Test weakref.WeakKeyDictionary()

class Foo:
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
