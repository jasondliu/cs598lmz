import weakref
# Test weakref.ref(foo) == weakref.ref(foo) where foo's lifetime ends.
class Foo:
    def __del__(self):
        print "del"

def test1():
    foo = Foo()
    r1 = weakref.ref(foo)
    r2 = weakref.ref(foo)
    foo.__dict__
    print "testing..."
    assert r1 == r2
    foo = None
    print "testing..."
    assert r1 == r2

def test2():
    foo = Foo()
    r1 = weakref.ref(foo)
    r2 = weakref.ref(foo)
    print "testing..."

test1()
test2()
