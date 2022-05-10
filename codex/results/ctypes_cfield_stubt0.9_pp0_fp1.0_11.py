import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
CStructure = type(S)

class CFields(collections.Mapping):
    def __init__(self, structure):
        self._structure = structure
        self._fields = {k: ctypes.Field(ctypes.c_void_p, k)
                        for k, _ in structure._fields_}

    def __getitem__(self, name):
        return self._fields[name]

    def __len__(self):
        return len(self._fields)

    def __iter__(self):
        return iter(self._fields)

def lazy(obj):
    if isinstance(obj, (tuple, list, array.array)):
        return tuple(map(lazy, obj))
    if isinstance(obj, collections.Mapping):
        return type(obj)((k, lazy(obj[k])) for k in obj)
    else:
        return obj

def compute(obj):
    if isinstance(obj, (tuple, list, array.array)):
        return type(obj)(map(compute, obj
