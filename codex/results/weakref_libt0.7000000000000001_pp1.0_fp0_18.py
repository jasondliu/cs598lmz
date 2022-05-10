import weakref
import os

class WeakKeyDictionary(dict):
    def __init__(self, *args, **kwargs):
        super(WeakKeyDictionary, self).__init__(*args, **kwargs)
        self.__dict__['_keys'] = weakref.WeakKeyDictionary()

    def __getitem__(self, key):
        return self._keys[key]

    def __setitem__(self, key, value):
        self._keys[key] = value

    def __delitem__(self, key):
        del self._keys[key]

    def __contains__(self, key):
        return key in self._keys

    def __iter__(self):
        return iter(self._keys)

    def __len__(self):
        return len(self._keys)

    def __repr__(self):
        return repr(dict(self.items()))

class WeakValueDictionary(dict):
    def __init__(self, *args, **kwargs):
        super(WeakValueDictionary, self).__init__(*
