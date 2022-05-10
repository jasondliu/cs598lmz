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
    print 'f:', l
    return l

def g():
    c = C('g')
    d = C('d')
    e = C('e')
    l = [c, d, e]
    print 'g:', l
    return l

def h():
    c = C('h')
    d = C('d')
    e = C('e')
    l = [c, d, e]
    print 'h:', l
    return l

def i():
    c = C('i')
    d = C('d')
    e = C('e')
    l = [c, d, e]
    print 'i:', l
    return
