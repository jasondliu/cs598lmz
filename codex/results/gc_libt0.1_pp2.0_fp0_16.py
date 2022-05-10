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
    c = C('test')
    print 'in test():', c
    return c

def test2():
    c = C('test2')
    print 'in test2():', c
    return c

def test3():
    c = C('test3')
    print 'in test3():', c
    return c

def test4():
    c = C('test4')
    print 'in test4():', c
    return c

def test5():
    c = C('test5')

