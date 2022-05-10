import gc, weakref

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
d['primary']                # entry was automatically removed

# The WeakValueDictionary class is a dictionary-like object that stores
# weak references to its values. When the only remaining references to
# a value are weak references, the key and value are automatically removed
# from the dictionary.

# WeakValueDictionary is useful for caching objects that are expensive to
# create, but can be re-created if necessary.

# The WeakValueDictionary class is a subclass of UserDict.UserDict.
# It overrides __setitem__() to create a weak reference to the value,
# and __getitem__
