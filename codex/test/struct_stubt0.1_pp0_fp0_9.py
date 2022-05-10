from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# Descriptors
class Descriptor:
    def __get__(self, instance, owner):
        print('Getting', self, instance, owner)
    def __set__(self, instance, value):
        print('Setting', self, instance, value)
    def __delete__(self, instance):
        print('Deleting', self, instance)

class Client:
    attr = Descriptor()

client = Client()
client.attr
client.attr = 'value'
del client.attr

# Properties
class Person:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


