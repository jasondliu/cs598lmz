import weakref
# Test weakref.ref()

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%r)' % self.name

def f(x):
    print 'f(%r)' % x

def g(x):
    print 'g(%r)' % x

def h(x):
    print 'h(%r)' % x

def test_ref():
    c = C('my object')
    r = weakref.ref(c, f)
    print 'should call f():', r
    r = weakref.ref(c, g)
    print 'should call g():', r
    r = weakref.ref(c, h)
    print 'should call h():', r
    print 'deleting c'
    del c
    print 'calling g() directly:'
    g(r)
    print 'calling h() directly:'
    h(r)
    print 'calling f() directly:'
    f(r)

def test_proxy():
   
