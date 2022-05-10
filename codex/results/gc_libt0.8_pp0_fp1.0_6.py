import gc, weakref

class Foo:
    pass

obj = Foo()
p = weakref.proxy(obj)

print(p)
print(p.__class__)

print(p.__doc__)
