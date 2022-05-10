import gc, weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%r)' % self.name

def f():
    c = C('f')
    d = C('d')
    e = C('e')
    l = [c, d]
    m = {'x': c, 'y': d}
    n = weakref.WeakKeyDictionary({c: 1, d: 2})
    o = weakref.WeakValueDictionary({'x': c, 'y': d})
    p = weakref.WeakSet([c, d])
    q = weakref.WeakValueDictionary({'x': c, 'y': d})
