from types import FunctionType
list(FunctionType(ObjectType(lambda: None)) == {})

FunctionType(ObjectType(lambda: None))({})

#desugar
"""
class MappingProxyType(object):
    __slots__ = ["_mapping"]

    def __init__(self, mapping):
        self._mapping = mapping

    def __repr__(self):
        return repr(self._mapping)

    def __getitem__(self, key):
        return self._mapping[key]

    def __setitem__(self, key, value):
        raise TypeError("'mappingproxy' object does not support item assignment")

    def get(self, key, default=None):
        return self._mapping.get(key, default)

    def copy(self):
        return self._mapping.copy()

    __copy__ = copy

    def keys(self):
        return KeysView(self._mapping)

    def items(self):
        return ItemsView(self._mapping)

    def values(self):
        return ValuesView(self._mapping)

    def __cont
