import weakref
# Test weakref.ref()

class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x

def f(x):
    return x

def g(x):
    return x.x

def h(x):
    return x.x.x

def k(x):
    return x.x.x.x

def l(x):
    return x.x.x.x.x

def m(x):
    return x.x.x.x.x.x

def n(x):
    return x.x.x.x.x.x.x

def o(x):
    return x.x.x.x.x.x.x.x

def p(x):
    return x.x.x.x.x.x.x.x.x

def q(x):
    return x.x.x.x.x.x.x.x.x.x

