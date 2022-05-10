import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def test_ref():
    f = Foo('bar')
    r = weakref.ref(f)
    print(r)
    print(r())
    del f
    print(r())

test_ref()

# Test weakref.proxy()

def test_proxy():
    f = Foo('bar')
    p = weakref.proxy(f)
    print(p)
    print(p.name)
    del f
    try:
        print(p.name)
    except ReferenceError:
        print('ReferenceError')

test_proxy()

# Test weakref.getweakrefcount()

def test_getweakrefcount():
    f = Foo('bar')
    r1 = weakref.ref(f)
    r2 = weakref.ref(f)
    print(weakref.getweakrefcount(f))

