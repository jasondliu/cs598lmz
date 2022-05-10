import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

o = MyClass('instance')
r = weakref.ref(o)
print r
print r()
print o

o2 = MyClass('instance2')
r2 = weakref.ref(o2)
print r2
print r2()
print o2

print 'before del o'
del o
print 'after del o'
print r()
print 'before del o2'
del o2
print 'after del o2'
print r2()

print 'before gc.collect()'
gc.collect()
print 'after gc.collect()'
print r()
print r2()
