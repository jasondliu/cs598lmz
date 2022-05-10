import gc, weakref
import sys

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive

del a                       # remove the one reference
gc.collect()                # run garbage collection right away

print d['primary']          # entry was automatically removed

try:
    d['primary']
except KeyError:
    print 'KeyError'

print '\n'

class B:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = B(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

a = B(9)                    # create a new instance
d['primary'] =
