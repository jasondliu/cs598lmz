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

# Metaclasses
class EntityMeta(type):
    def __new__(meta, name, bases, class_dict):
        print('In Meta.new: ', meta, name, bases, class_dict)
        return type.__new__(meta, name, bases, class_dict)

class Entity(metaclass=EntityMeta):
    def __init__(self, size):
        self.size = size
        super().__init__()

e = Entity(10)
print
