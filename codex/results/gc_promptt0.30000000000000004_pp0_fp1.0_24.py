import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# gc.collect()

class MyClass(object):
    def __init__(self, name):
        self.name = name
        print 'Created', self.name

    def __repr__(self):
        return '<Instance of %s, name=%s>' % (self.__class__.__name__, self.name)

    def __del__(self):
        print 'Deleted', self.name

def test():
    a = MyClass('a')
    b = MyClass('b')
    a.b = b
    b.a = a
    del a
    del b

test()
gc.collect()
print '-' * 20

# Test weakref
a = MyClass('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
print d['primary']
del a
gc.collect()
print d['primary']
print '-' * 20

# Test weakref.ref()
a = MyClass('a')
b = MyClass('b')
a.b = b
b
