import weakref
# Test weakref.ref()
def f():
    return 42

w = weakref.ref(f)
print(w())
# Test weakref.ref(o)
class Foo:
    def __init__(self, x):
        self.x = x

foo = Foo(42)
w = weakref.ref(foo)
print(w().x)
# Test weakref.ref(o, cb)
l = []
def cb(r):
    l.append(r)

class Foo:
    def __init__(self, x):
        self.x = x

foo = Foo(42)
w = weakref.ref(foo, cb)
print(w().x)
del foo
print(w())
print(l[0]())
# Test weakref.ref(o, cb)
class Foo:
    def __init__(self, x):
        self.x = x

foo = Foo(42)
w = weakref.ref(foo, lambda r: None)
print(w().x)
del foo
print(w())

