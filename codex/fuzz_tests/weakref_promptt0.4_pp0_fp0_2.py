import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    pass

foo = Foo()
foo.x = 1

r = weakref.ref(foo)
p = weakref.proxy(foo)

print(r(), p.x)

del foo

print(r(), p.x)
