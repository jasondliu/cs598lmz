import gc, weakref

class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)       # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive

del a                       # remove the one reference
gc.collect()                # run garbage collection right away

print(d['primary'])         # entry was automatically removed
print(d)

# 10
# WeakValueDictionary()

# The WeakValueDictionary class is similar to a standard dictionary, except that values are weak references.
# When the only remaining references to a value are weak references, garbage collection is free to destroy the value and reclaim its memory.
# When this happens, the corresponding key is automatically removed from the weak dictionary.
# This makes weak dictionaries useful for caching objects that are expensive to create, and also have a short lifetime.
# A common use case is caching the results of a database query
