import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldType = type(ctypes.c_int)

class CField(ctypes.CField):
    def __new__(self, *args):
        return ctypes.CField.__new__(self, *args)

    def __init__(self, *args):
        print("__init__")
        print("args: ", *args)
        ctypes.CField.__init__(self, *args)

    def __repr__(self):
        return ctypes.CField.__repr__(self) + " __repr__"

    def __get__(self, obj, type=None):
        print("__get__")
        print(type(obj), type)
        res = ctypes.CField.__get__(self, obj, type)
        print(type(res), res)
        return res

    def __set__(self, obj, value):
        print("__set__")
        return ctypes.CField.__set__(self, obj, value)

print(type(ctypes.
