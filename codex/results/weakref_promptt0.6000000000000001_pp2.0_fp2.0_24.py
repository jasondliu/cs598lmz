import weakref
# Test weakref.ref(x).__call__()

class Foo(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

class Bar(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

def test(x):
    print 'x:', x
    print 'ref(x):', weakref.ref(x)
    print 'ref(x)():', weakref.ref(x)()

test(Foo(42))
test(Bar(42))

# Test weakref.ref(x).__call__() on a subtype of a built-in type

class MyInt(int):
    pass

class MyFloat(float):
    pass

def test_int(x):
    print 'x:', x
    print 'ref(x):', weakref.ref(x)
    print 'ref(x)():', weakref.ref(x)()

test_int
