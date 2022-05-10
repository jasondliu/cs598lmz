import gc, weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name

def f():
    o = C('f')
    print 'in f(): o =', o
    return o

def g():
    o = C('g')
    print 'in g(): o =', o
    return o

def h():
    o = C('h')
    print 'in h(): o =', o
    return o

def show_chain(obj, chain):
    for i, link in enumerate(chain):
        o = link()
        if o is None:
            print '%d: dead' % i
        else:
            print '%d: %s' % (i, o)

print 'creating cycle...'
x = f()
y = g()
z = h()

x.next = y
y.next = z
z.next = x

print 'cleaning up...'
del x,
