import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo:
    pass

foo = Foo()

def test():
    return weakref.ref(foo) == weakref.ref(foo)

print(test())
