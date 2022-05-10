import gc, weakref

from collections import OrderedDict

class WeakOrderedSet(OrderedDict):
    def __init__(self, *args, **kwargs):
        super(WeakOrderedSet, self).__init__(*args, **kwargs)
        self.__dict__['_refs'] = {}

    def __setitem__(self, key, value):
        if value is None:
            return
        if key in self._refs:
            self._refs[key].append(weakref.ref(value))
        else:
            self._refs[key] = [weakref.ref(value)]
        super(WeakOrderedSet, self).__setitem__(key, value)

    def __getitem__(self, key):
        if key in self:
            return super(WeakOrderedSet, self).__getitem__(key)
        else:
            if key in self._refs:
                for ref in self._refs[key]:
                    value = ref()
