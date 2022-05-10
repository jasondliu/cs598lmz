from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f'))

# %%
# 使用元类
class EntityMeta(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Entity':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: {}'.format(name))
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: {} ==> {}'.format(k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str
