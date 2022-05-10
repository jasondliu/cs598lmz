import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print d['primary']
del a
gc.collect()
print d['primary']

# 10
# 10

# WeakValueDictionary objects behave like dictionaries with one difference:
# values are held weakly. When the only reference to a value is a weak reference,
# the entry is automatically removed from the dictionary.

# WeakValueDictionary is a mapping class that stores only weak references to its
# values. This can be used to store objects in a cache without increasing the
# reference count, and hence without preventing the referenced object from being
# garbage collected.

# If a referenced object is garbage collected elsewhere, the corresponding entry
# in the WeakValueDictionary is automatically removed.

# This is useful for caching objects without adding to their reference counts.
# A WeakValueDictionary is a mapping class that stores only weak references
