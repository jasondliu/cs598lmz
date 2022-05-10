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
print d.items()
del a
print 'after del a'
print d.items()

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before del a'
print d.items()
del a
print 'after del a'
print d.items()

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before del a'
print d.items()
del a
print 'after del a'
print d.items()

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before del a'
print d.items()
del a
print 'after
