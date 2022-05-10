import gc, weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
        print 'Created', self.name
    def __del__(self):
        print 'Destroyed', self.name

def f():
    a = Foo('a')
    b = Foo('b')
    c = Foo('c')
    d = Foo('d')
    e = Foo('e')
    f = Foo('f')
    g = Foo('g')
    h = Foo('h')
    i = Foo('i')
    j = Foo('j')
    k = Foo('k')
    l = Foo('l')
    m = Foo('m')
    n = Foo('n')
    o = Foo('o')
    p = Foo('p')
    q = Foo('q')
    r = Foo('r')
    s = Foo('s')
    t = Foo('t')
    u = Foo('u')
    v = Foo('v')
    w = Foo('w')
    x = Foo('x')
    y = Foo
