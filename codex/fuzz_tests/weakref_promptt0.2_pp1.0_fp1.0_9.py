import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'Goodbye,', self.name

b = Foo('b')
d = weakref.ref(b)
print d()
print d() is b
print d() is None
del b
print d() is None

# Test weakref.proxy()

class Foo:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'Goodbye,', self.name

b = Foo('b')
p = weakref.proxy(b)
print p.name
print p.name == b.name
print p is b
print p == b
print p is None
print p == None
del b
print p is None
print p == None

# Test weakref.WeakKeyDictionary()

class Foo:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'Goodbye,
