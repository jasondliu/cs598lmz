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

