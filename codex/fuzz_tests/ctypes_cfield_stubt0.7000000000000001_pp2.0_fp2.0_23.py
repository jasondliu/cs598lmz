import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Example(ctypes.CField):
    def __init__(self, *args, **kwds):
        print "__init__"
        super(Example, self).__init__(*args, **kwds)
    def __getitem__(self, key):
        print "__getitem__", key
        return super(Example, self).__getitem__(key)
    def __setitem__(self, key, value):
        print "__setitem__", key, value
        return super(Example, self).__setitem__(key, value)
    def __getattr__(self, key):
        print "__getattr__", key
        return super(Example, self).__getattr__(key)
    def __setattr__(self, key, value):
        print "__setattr__", key, value
        return super(Example, self).__setattr__(key, value)
    def __repr__(self):
        print "__repr__"
        return super(Example, self).__repr__()

s = S
