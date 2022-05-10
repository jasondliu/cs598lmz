import gc, weakref

class Foo(object):
    pass

foo = Foo()
f = weakref.ref(foo)

print(f)
print(f())
print(f() is foo)

del foo
print(gc.collect())
print(f())
