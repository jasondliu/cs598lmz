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
# 10
del a                  # remove the one reference
gc.collect()            # run garbage collection right away
# 0
d['primary']            # entry was automatically removed
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     KeyError: 'primary'

# WeakKeyDictionary

# A WeakKeyDictionary is a mapping class that holds only weak references to its keys.
# If a key is no longer used anywhere else, it will be automatically removed from the dictionary.

# WeakKeyDictionaries are useful when you need to associate additional data with an object owned by other parts of an application without adding attributes to those objects.
#
