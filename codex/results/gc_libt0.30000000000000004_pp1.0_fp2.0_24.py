import gc, weakref

class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before:', d.data
a = None
gc.collect()
print 'after:', d.data
