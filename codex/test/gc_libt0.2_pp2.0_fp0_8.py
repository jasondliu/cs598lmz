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
    l = [c, d, e]
