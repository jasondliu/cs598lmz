import weakref


class WeakValueDict(object):
    # A weak reference to a key that is not traceable by gc
    _Nothing = object()

    def __init__(self):
        self._dict = {}

    def _make_weakref(self, obj):
        return weakref.proxy(obj, lambda wr: self._cleanup(obj))

    def _cleanup(self, obj):
        try:
            del self._dict[obj]
        except KeyError:
            pass

    def __getitem__(self, item):
        return self._dict[item]

    def __setitem__(self, key, value):
        self._dict[key] = self._make_weakref(value)

    def __delitem__(self, key):
        del self._dict[key]

    def __contains__(self, item):
        return item in self._dict

    def __iter__(self):
        for key, value in self._dict.iteritems():
            try:
                item = value()
            except ReferenceError:
                item = None

