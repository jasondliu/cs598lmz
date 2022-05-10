import gc, weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name

def f():
    c = C('f')
    print 'in f():', c
    return c

def g():
    c = C('g')
    print 'in g():', c
    return c

def h():
    c = C('h')
    print 'in h():', c
    return c

def test():
    c = f()
    print 'in test():', c
    return c

def test2():
    c = f()
    print 'in test2():', c
    return c

def test3():
    c = f()
    print 'in test3():', c
    return c

def test4():
    c = f()
    print 'in test4():', c
    return c

def test5():
    c = f()
    print 'in test5():', c
    return c

