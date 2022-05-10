import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a       # does not create a reference
print(d['primary'])    # fetch the object if it is still alive
del a                  # remove the one reference
gc.collect()           # run garbage collection right away
print(d['primary'])    # entry was automatically removed
# Test gc.get_referrers()
class Graph:
    def __init__(self, name):
        self.name = name
        self.other = None
    def set_next(self, other):
        print('Connecting', self, 'to', other)
        self.other = other
    def all_connected(self):
        yield self.name
        other = self.other
        while other:
            yield other.name
            other = other.other
    def __repr__(self
