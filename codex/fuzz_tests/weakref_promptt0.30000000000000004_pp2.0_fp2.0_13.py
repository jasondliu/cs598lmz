import weakref
# Test weakref.ref.__init__()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print 'callback(%r)' % r

def test():
    f = Foo('bar')
    r = weakref.ref(f, callback)
    print 'r =', r
    print 'f =', f
    print 'r() =', r()
    print 'f is r() =', f is r()
    print 'deleting f'
    del f
    print 'r() =', r()
    print 'r() is None =', r() is None
    print 'f = Foo("baz")'
    f = Foo('baz')
    print 'r() =', r()
    print 'f is r() =', f is r()
    print 'f = Foo("quux")'
    f = Foo('quux')
    print 'r() =', r()
    print '
