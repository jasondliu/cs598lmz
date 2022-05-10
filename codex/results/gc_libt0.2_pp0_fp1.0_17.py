import gc, weakref

class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before del a'
print d['primary']
print d
del a
print 'after del a'
print d['primary']
print d
print 'gc.collect()'
gc.collect()
print d['primary']
print d

print '\n\n'

a = A(10)
d = weakref.WeakKeyDictionary()
d[a] = 'primary'
print 'before del a'
print d[a]
print d
del a
print 'after del a'
print d[a]
print d
print 'gc.collect()'
gc.collect()
print d[a]
print d
