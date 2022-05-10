import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print 'callback(%r)' % r

a = Foo('a')
d = weakref.WeakKeyDictionary()
d[a] = 1
r = weakref.ref(a, callback)
print 'before:', d.items()
del a
print 'after:', d.items()

# Test weakref.WeakValueDictionary

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print 'callback(%r)' % r

a = Foo('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
r = weakref.ref(a, callback)
print 'before:', d.items()
