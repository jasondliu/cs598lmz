import gc, weakref

class A(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name
    def __del__(self):
        print 'del', self

a = A('a')
b = A('b')
c = A('c')

d = weakref.WeakValueDictionary()
d['primary'] = a
d['secondary'] = b
d['tertiary'] = c

print 'before, d.data:', d.data
print 'before, d.items():', d.items()

del a
del b
del c

print 'after, d.data:', d.data
print 'after, d.items():', d.items()

gc.collect()

print 'collected, d.data:', d.data
print 'collected, d.items():', d.items()

print 'd["primary"]:', d['primary']
print 'd["secondary"]:', d['secondary']
print 'd["
