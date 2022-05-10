import gc, weakref

class A(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name

a = A('a')
b = A('b')
c = A('c')

d = weakref.WeakValueDictionary()
d['primary'] = a
d['secondary'] = b
d['tertiary'] = c

print 'before, d.data:', d.data
del a
print 'after, d.data:', d.data
del b
print 'removing "secondary", d.data:', d.data
del c
print 'removing "tertiary", d.data:', d.data

print '\n'

class B(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'B(%s)' % self.name

a = B('a')
b = B('b')
c = B('c')

d
