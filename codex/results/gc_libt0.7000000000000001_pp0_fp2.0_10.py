import gc, weakref

class SomeClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'SomeClass(%s)' % self.name

print 'creating SomeClass instances'
obj1 = SomeClass('obj1')
obj2 = SomeClass('obj2')

print 'weakrefing SomeClass instances'
r1 = weakref.ref(obj1)
r2 = weakref.ref(obj2)

print 'deleting SomeClass instances'
del obj1
del obj2

print 'testing dereferencing weakrefs'
print r1(), r2()

print 'garbage collecting'
gc.collect()
print r1(), r2()
