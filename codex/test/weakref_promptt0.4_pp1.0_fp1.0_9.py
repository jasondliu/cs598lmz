import weakref
# Test weakref.ref(obj)

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name

def f():
    x = C('x')
    y = C('y')
    x.y = y
    y.x = x
    return weakref.ref(x), weakref.ref(y)

xr, yr = f()
