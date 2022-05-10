import weakref
# Test weakref.ref(obj, callback)

import weakref

def callback(x):
    print 'callback(', x, ')'

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def test(callback):
    f = Foo('f')
    r = weakref.ref(f, callback)
    print 'created weak reference', r
    print 'callback should not be called yet'
    print 'deleting f'
    del f
    print 'callback should be called now'

print 'testing with a function'
test(callback)

print 'testing with a method'
test(Foo.__repr__)

print 'testing with an instance method'
test(Foo('f').__repr__)

print 'testing with an instance'
test(Foo('f'))
