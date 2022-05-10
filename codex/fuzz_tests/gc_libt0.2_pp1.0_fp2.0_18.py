import gc, weakref

class A(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'del', self.name

def test():
    a = A('a')
    b = A('b')
    c = A('c')
    d = A('d')
    e = A('e')
    f = A('f')
    g = A('g')
    h = A('h')
    i = A('i')
    j = A('j')
    k = A('k')
    l = A('l')
    m = A('m')
    n = A('n')
    o = A('o')
    p = A('p')
    q = A('q')
    r = A('r')
    s = A('s')
    t = A('t')
    u = A('u')
    v = A('v')
    w = A('w')
    x = A('x')
    y = A('y')
    z = A('z
