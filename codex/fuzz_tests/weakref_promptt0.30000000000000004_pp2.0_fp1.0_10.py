import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def callback(r):
    print 'callback(', r, ')'

def test_ref(name):
    o = Foo(name)
    r = weakref.ref(o, callback)
    print 'o =', o
    print 'r =', r
    print 'r() =', r()
    print 'o =', o
    print 'deleting o'
    del o
    print 'r() =', r()
    print 'r =', r

test_ref('a')
print
test_ref('b')

# Test weakref.proxy()

def test_proxy(name):
    o = Foo(name)
    p = weakref.proxy(o, callback)
    print 'o =', o
    print 'p =', p
    print 'p.name =', p.name
    print 'o =', o
