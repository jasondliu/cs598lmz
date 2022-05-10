import gc, weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name

def f():
    c = C('f')
    print c
    return c

def g():
    c = C('g')
    print c
    return c

def h():
    c = C('h')
    print c
    return c

def i():
    c = C('i')
    print c
    return c

def j():
    c = C('j')
    print c
    return c

def k():
    c = C('k')
    print c
    return c

def l():
    c = C('l')
    print c
    return c

def m():
    c = C('m')
    print c
    return c

def n():
    c = C('n')
    print c
    return c

def o():
    c = C('o')
    print c

