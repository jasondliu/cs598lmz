import weakref
# Test weakref.ref()

class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x

def f(x):
    return C(x)

def g(x):
    return lambda: x

def h(x):
    class D:
        def __repr__(self):
            return 'D(%r)' % x
    return D()

def test(f, x):
    print f, x
    r = weakref.ref(f(x))
    print 'initial:', r, r()
    for i in range(5):
        print 'step', i
        gc.collect()
        print '   ', r, r()
    print

test(f, 1)
test(g, 2)
test(h, 3)

# Test weakref.proxy()

class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return '
