import gc, weakref
from . import _weakref

class WeakValueDictionary(_weakref.WeakValueDictionary):
    """Mapping class that references values weakly.

    Entries in the dictionary will be discarded when no strong
    reference to the value exists anymore.
    """

    def __init__(*args, **kw):
        if not args:
            raise TypeError("descriptor '__init__' of 'WeakValueDictionary' object "
                            "needs an argument")
        self, *args = args
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        if args:
            dict = args[0]
        else:
            dict = None
        self.data = weakref.WeakValueDictionary()
        if dict is not None:
            self.update(dict)

    def __getitem__(self, key):
        o = self.data[key]()
        if o is None:
            raise KeyError(key)
        else:
            return o

    def __contains__(self
