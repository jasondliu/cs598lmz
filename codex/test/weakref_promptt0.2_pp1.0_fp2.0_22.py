import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo:
    pass

foo = Foo()

def test():
    ref1 = weakref.ref(foo)
    ref2 = weakref.ref(foo)
    assert ref1 == ref2

test()
print("passed")
