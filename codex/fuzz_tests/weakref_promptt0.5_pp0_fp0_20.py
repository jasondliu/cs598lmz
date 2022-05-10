import weakref
# Test weakref.ref
import gc
import weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def func(obj):
    print 'func:', obj()

def callback(obj):
    print 'callback:', obj()

f = Foo('f')
# Create a weak reference
r = weakref.ref(f, callback)
r() is f
r() is None
f = None
r() is None

f = Foo('f')
r = weakref.ref(f, callback)
f = None
gc.collect()

f = Foo('f')
r = weakref.ref(f, func)
f = None
gc.collect()

# Test weakref.WeakKeyDictionary
class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback
