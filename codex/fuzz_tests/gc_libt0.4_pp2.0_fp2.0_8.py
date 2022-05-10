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

del o
gc.collect()
print r()

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name
    def __del__(self):
        print 'MyClass.__del__(%s)' % self.name

o = MyClass('instance')
r = weakref.ref(o)
print r
print r()
print o

del o
gc.collect()
print r()

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%
