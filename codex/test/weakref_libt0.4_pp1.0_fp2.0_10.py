import weakref

class _WeakSet(collections.MutableSet):
    """A set that stores weak references to its elements.

    All elements must be hashable.  Unhashable elements will raise a
    TypeError.

    """

    def __init__(self, data=None):
        self.data = weakref.WeakKeyDictionary()
        if data is not None:
            self |= data

    def __contains__(self, key):
        return key in self.data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def add(self, elem):
        self.data[elem] = None

    def discard(self, elem):
        try:
            del self.data[elem]
        except KeyError:
            pass

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, list(self))

