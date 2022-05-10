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
d = weakref.WeakValueDictionary()
d['primary'] = a
r = weakref.ref(a, callback)
print 'before:', d
del a
print 'after:', d
print 'r:', r
print 'r():', r()

# Test weakref.proxy()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

a = Foo('a')
p = weakref.proxy(a)
print 'before:', p
del a
print 'after:', p
