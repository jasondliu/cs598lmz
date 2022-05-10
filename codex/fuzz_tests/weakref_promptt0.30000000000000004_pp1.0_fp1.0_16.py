import weakref
# Test weakref.ref()

import weakref

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(reference):
    print 'callback(', reference, ')'

f = Foo('f')
r = weakref.ref(f, callback)
print 'created:', r
print 'f:', f
print 'r():', r()
print

f = None
print 'deleted f'
print 'r():', r()
print

import gc
gc.collect()
print 'collected'
print 'r():', r()
print

print 'end of script'
