import weakref
# Test weakref.ref

def f(x):
    return x

x = "test"
r = weakref.ref(x, f)
print(r)
del x
print(r())

# Test weakref.proxy

class Foo(object):
    def __init__(self):
        self.bar = 42
    def __repr__(self):
        return "Foo()"

foo = Foo()
p = weakref.proxy(foo)
print(p)
print(p.bar)
del foo
print(p)
print(p.bar)
