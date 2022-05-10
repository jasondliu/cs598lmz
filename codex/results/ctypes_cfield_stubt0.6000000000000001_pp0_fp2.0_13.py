import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFields(object):
    def __init__(self, fields):
        self.fields = fields
    def __getitem__(self, key):
        return CFields([(k, v) for k, v in self.fields if k == key])
    def __setitem__(self, key, value):
        for k, v in self.fields:
            if k == key:
                if isinstance(v, ctypes.CField):
                    v.__set__(self, value)
                else:
                    v[0] = value
                break
    def __len__(self):
        return len(self.fields)
    def __iter__(self):
        for k, v in self.fields:
            if isinstance(v, ctypes.CField):
                yield (k, v.__get__(self))
            else:
                yield (k, v[0])

def make_cfields(cls):
    fields = []
    for k, v in cls.__dict__.items():
        if isinstance(
