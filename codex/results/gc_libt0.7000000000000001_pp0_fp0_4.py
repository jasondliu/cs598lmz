import gc, weakref

#
#    This file contains a simple object garbage collector.
#    It uses weak references, so the object will live as long as there
#    is a strong reference to it.  But if it is deleted, the weak
#    reference will be deleted too.
#

#
#   Weak references cannot be used directly as the keys in a dictionary.
#   The object is not removed from the dictionary if the weak reference
#   is deleted.
#
#   The class WeakDictionary wraps a normal dictionary using weak references
#   for the keys.  The functionality of a normal dictionary is retained.
#

class WeakDictionary:

    def __init__(self):
        self.dict = {}
        self._refs = weakref.WeakValueDictionary()
        return

    def __getitem__(self, key):
        try:
            return self._refs[key]
        except KeyError:
            return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value
        self._refs[key] = value
