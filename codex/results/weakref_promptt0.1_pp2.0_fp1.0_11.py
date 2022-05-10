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

del f
print(p)
