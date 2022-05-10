import gc, weakref, sys

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)               # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a        # does not create a reference
d['primary']            # fetch the object if it is still alive
del a                   # remove the one reference
gc.collect()            # run garbage collection right away

d['primary']            # entry was automatically removed

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

d['primary'] = a
d['primary']

del a
d['primary']

gc.collect()

d['primary']

try:
    d['primary']
except KeyError:
    print('KeyError')

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

d['primary'] =
