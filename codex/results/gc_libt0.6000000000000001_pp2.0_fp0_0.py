import gc, weakref

class Foo(object):
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return 'Foo(%s)' % self.val

def bar(obj):
    print 'in bar()'
    print 'refcount =', sys.getrefcount(obj)

a = Foo(1)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['secondary'] = a
print 'before del a'
bar(a)
del a
print 'after del a'
gc.collect()
bar(d['primary'])
print d['primary']
