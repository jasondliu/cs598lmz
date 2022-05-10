import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

class Nested(object):
    """
    A nested descriptor
    """
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data_type(instance.__dict__[self.name])

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class NestedMeta(type):
    """
    Metaclass for nested descriptors
    """
    def __new__(mcs, name, bases, attrs):
        for key, value in attrs.items():
            if isinstance(value, Nested):
                attrs[key] = Nested(key, value.data_type)
        return type.__new__(m
