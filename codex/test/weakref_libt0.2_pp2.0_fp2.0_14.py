import weakref

from . import _base


class _WeakKeyDictionary(_base.WeakKeyDictionary):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._refs = weakref.WeakKeyDictionary()

    def __setitem__(self, key, value):
        self._refs[key] = weakref.ref(value)
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return self._refs[key]()

    def __delitem__(self, key):
        del self._refs[key]
        super().__delitem__(key)

    def __contains__(self, key):
        return key in self._refs

    def __iter__(self):
        return iter(self._refs)

    def __len__(self):
        return len(self._refs)

