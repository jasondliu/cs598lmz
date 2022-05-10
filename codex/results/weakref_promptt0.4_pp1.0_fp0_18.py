import weakref
# Test weakref.ref(obj, callback)

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

    def __del__(self):
        print 'deleting Foo %r' % self.name

def callback(ref):
    print 'callback(%r)' % ref

f = Foo('f')
r = weakref.ref(f, callback)
print 'created object:', f
print 'created weak reference:', r
print 'deleting f'
del f
print 'r.alive:', r.alive
print 'clearing r'
r.clear()
print 'r.alive:', r.alive
print 'deleting r'
del r
print 'r.alive:', r.alive

# Test weakref.ref(obj, callback, kwarg1=value1, ...)

class Foo:
    def __init__(self, name):
        self.name = name
    def __re
