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

