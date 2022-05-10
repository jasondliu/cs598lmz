import types
types.add_to(types.InstanceType, '__getitem__')
types.add_to(types.InstanceType, '__setitem__')
types.add_to(types.InstanceType, '__contains__')
types.add_to(types.InstanceType, '__delitem__')
types.add_to(types.InstanceType, '__iter__')

def get_type_item(self, key):
    return getattr(self, key)
type_item.implicit = get_type_item

def set_type_item(self, key, value):
    setattr(self, key, value)
type_item.implicit = set_type_item

def contains_type(self, value):
    return self.__contains__(value)
type_contains.implicit = contains_type

def iter_type(self):
    return self.__iter__()
type_iter.implicit = iter_type
