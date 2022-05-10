import gc, weakref

class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'Before:', d.data
a = None
print 'After:', d.data

del a
print 'After:', d.data

gc.collect()
print 'After:', d.data
