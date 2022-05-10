import weakref
# Test weakref.ref()

class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)
print r
print r()

f = None
print r()

print '-' * 20

# Test weakref.proxy()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

f = Foo('f')
p = weakref.proxy(f)
print p
print p.name

f = None
print p.name
