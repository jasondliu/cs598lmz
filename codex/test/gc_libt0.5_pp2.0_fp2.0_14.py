import gc, weakref, sys

class Weak(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<Weak referencing {!r}>'.format(self.value)

a = Weak(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

# _remove() is called when the weakly referenced object is about to be
# finalized.
def _remove(ref):
    print('_remove({!r})'.format(ref))
    print('  dict:', d)

weakref.finalize(a, _remove)

# del a
# del d

# gc.collect()
# print(gc.garbage)

# del a
# del d
# gc.collect()
# print(gc.garbage)

# del a
# gc.collect()
# print(gc.garbage)

# del d
# gc.collect()
# print(gc.garbage)

# print(sys.get
