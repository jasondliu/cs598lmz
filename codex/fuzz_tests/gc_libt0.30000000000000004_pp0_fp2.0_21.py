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

print 'deleting o'
del o
print gc.collect()
print r()

print 'creating a new instance'
o = MyClass('new instance')
print r()

print 'deleting o again'
del o
print gc.collect()
print r()

print 'creating a new instance again'
o = MyClass('new instance again')
print r()

print 'deleting r'
del r
print gc.collect()
print o
