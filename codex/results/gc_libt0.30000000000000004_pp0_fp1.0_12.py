import gc, weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'C.__del__', self.name

def f():
    c = C('f')
    print 'f:', c
    return c

def g():
    c = C('g')
    print 'g:', c
    return c

def h():
    c = C('h')
    print 'h:', c
    return c

def i():
    c = C('i')
    print 'i:', c
    return c

def j():
    c = C('j')
    print 'j:', c
    return c

def k():
    c = C('k')
    print 'k:', c
    return c

def l():
    c = C('l')
    print 'l:', c
    return c

def m():
    c = C('m')
    print 'm:', c
    return c

def n():
    c
