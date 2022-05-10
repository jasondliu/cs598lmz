import weakref
# Test weakref.ref(obj, callback)

import weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%r)' % self.name

def callback(r):
    print 'callback(', r, ')'

a = C('a')
r = weakref.ref(a, callback)
print 'r =', r
print 'r() =', r()
print 'deleting a'
del a
print 'r() =', r()
print 'r() is None?', r() is None

# Test weakref.ref(obj, callback) with a class instance

import weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%r)' % self.name

def callback(r):
    print 'callback(', r, ')'

a = C('a')
r = weakref.ref(a, callback)
print
