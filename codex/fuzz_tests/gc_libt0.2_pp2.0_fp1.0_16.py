import gc, weakref

class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before del a'
print d['primary']
del a
gc.collect()
print 'after del a'
print d['primary']

# before del a
# 10
# after del a
# 10

# Note that the object is still there after the del a, but it will be deleted
# when the garbage collector runs.

# The WeakKeyDictionary works similarly, but uses the keys of the dictionary
# as weak references.

# The WeakValueDictionary and WeakKeyDictionary classes also accept a
# callback function that is called when a key or value is deleted from the
# dictionary.

# Weak references can be used to implement caches. If the cache is not
# limited in size, it can grow indefinitely, which is not a good thing.
# Using a WeakValueDictionary, you
