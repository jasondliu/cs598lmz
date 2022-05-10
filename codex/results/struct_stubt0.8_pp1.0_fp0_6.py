from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(dict(format='Pc'))
s.size = s.__sizeof__()
s

class MyStruct(Struct):
    _fields_ = [('a', 'P'), ('b', 'c')]
    
type(_fields_)
MyStruct.format
struct.calcsize(MyStruct.format)

# 元类使用
from collections import OrderedDict
from keyword import iskeyword

def make_struct_class(typename, field_names, verbose=False):
    field_names = list(field_names)
    for name in field_names:
        if iskeyword(name):
            raise TypeError('Invalid struct field name %r' % name)
    if verbose:
        print('Field name: %r.' % field_names)
    field_names = tuple(field_names)
    def __init__(self, *args, **kwargs):
        if verbose:
            print('args: %r, kwargs: %r.' % (args, k
