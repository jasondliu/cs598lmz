import ctypes
ctypes.cast(0, ctypes.py_object)

s = 'I am a string'
print(s)

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._fields = [name for name, _ in cls._fields_]
        cls._fields_dict = dict(cls._fields_)
        cls._len = len(cls._fields)
    def __getitem__(cls, item):
        if isinstance(item, int):
            return cls._fields[item]
        return cls._fields_dict[item]

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields_ = []
    def __new__(cls, *args):
        if len(args) != cls._len:
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)

class Stock(StructTuple
