import types
types.TypeType

_GRAPH_ATTRS = ['name', 'device', 'initializer', 'dtype',
                'seed', 'shape', 'graph', 'colocation_groups']


class _SeededDict(object):
    """A dict-like object that can be but isn't a dict.

    This is used so that a node can both behave as a list in some
    contexts and still be hashable.
    """

    def __init__(self, *args):
        if not args:
            self._d = dict()
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, dict):
                self._d = arg
            else:
                self._d = dict(*args)
        else:
            self._d = dict(*args)

    def __len__(self):
        return len(self._d)

    def __getitem__(self, item):
        return self._d[item]

    def __setitem__(self, key, value):
        self._d[key] = value


