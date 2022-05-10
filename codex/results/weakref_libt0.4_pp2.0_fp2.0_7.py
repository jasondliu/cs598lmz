import weakref

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
o = None
print r()
print r

print '-'*30

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
r = None
print o
print r

print '-'*30

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

o = MyClass('instance')
r =
