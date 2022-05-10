import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self):
        self._objects = {}

    def __getitem__(self, key):
        return self._objects[key]

    def __setitem__(self, key, value):
        if not isinstance(value, ctypes.CField):
            raise TypeError("must be a ctypes.CField")
        self._objects[key] = value

    def __delitem__(self, key):
        del self._objects[key]

    def __iter__(self):
        return iter(self._objects)

    def __len__(self):
        return len(self._objects)
</code>

