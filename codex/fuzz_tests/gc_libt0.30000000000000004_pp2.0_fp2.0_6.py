import gc, weakref
from collections import defaultdict

class WeakKeyDictionary(object):
    def __init__(self):
        self._data = weakref.WeakKeyDictionary()

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __contains__(self, key):
        return key in self._data

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)

    def __str__(self):
        return str(self._data)

    def __eq__(self, other):
        return self._data == other

    def __ne__(self, other):
        return self._data != other

    def __lt__(self, other):
        return self._data < other
