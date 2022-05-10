import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo(object):
    pass

obj = Foo()

def test(obj):
    r1 = weakref.ref(obj)
    r2 = weakref.ref(obj)
    print r1 is r2

test(obj)

test(1)

test("hello")

test(None)

test(test)

test(r1)

test(r2)

test(Foo)

test(Foo())

test(Foo)

test(Foo())

test(Foo)

test(Foo())

test(Foo)

test(Foo())

test(Foo)

test(Foo())

test(Foo)

test(Foo())

test(Foo)

test(Foo())

test(Foo)

test(Foo())

test(Foo)

test(Foo())

test(Foo)

test(Foo())

test(F
