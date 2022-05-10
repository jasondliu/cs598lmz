import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print('callback(%r)' % r)

a = Foo('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
r = weakref.ref(a, callback)
print('before:', r, r())
print('dictionary:', d)
a = 'something else'
print('after:', r, r())
print('dictionary:', d)

# Test weakref.WeakValueDictionary()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

a = Foo('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
print('dictionary:', d)
a = 'something else'
