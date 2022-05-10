import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name

def f():
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
    z
