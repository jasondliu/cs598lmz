import gc, weakref, sys

class A(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name

a = A('a')
b = A('b')
a.b = b
b.a = a

print 'Before'
print 'a:', sys.getrefcount(a)
print 'b:', sys.getrefcount(b)

print 'After'
del a
del b
print 'a:', sys.getrefcount(a)
print 'b:', sys.getrefcount(b)

print 'a:', gc.get_referents(a)
print 'b:', gc.get_referents(b)

print 'a:', gc.get_referrers(a)
print 'b:', gc.get_referrers(b)

print 'a:', gc.get_referrers(a, weakref.CallableProxyType)
print 'b:', gc
