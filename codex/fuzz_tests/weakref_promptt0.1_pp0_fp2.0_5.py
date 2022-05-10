import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(r)
print(r())

del f
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

# Test weakref.getweakrefcount()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(weakref.getweakrefcount(f))

del f
print(weakref.getweakrefcount(r))

# Test weakref.getweakrefs()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(weakref.getweakrefs(f))

del f
print(weakref.getweakrefs(r))

# Test weakref.finalize()

class Foo:
    pass

f = Foo
