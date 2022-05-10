import gc, weakref
import sys
import time

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def show_refs(message, refs):
    print message
    for ref in refs:
        obj = ref()
        if obj is not None:
            print 'object referenced by %s: %s' % (ref, obj)
        else:
            print 'object referenced by %s has been garbage collected' % ref

a = Foo('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
d['alias'] = a

print 'd =', d
show_refs('d.items()', d.items())

del a
print '\ndel a'
show_refs('d.items()', d.items())

print '\ngc.collect()'
n = gc.collect()
print 'Unreachable objects:', n
show_refs('d.items()', d
