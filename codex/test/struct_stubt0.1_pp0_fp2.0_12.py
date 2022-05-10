from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# Descriptors

class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        print('Get', self.name)

    def __set__(self, instance, value):
        print('Set', self.name, value)


class SubDescriptor(Descriptor):
    def __get__(self, instance, cls):
        print('Sub Get', self.name)


class ClientClass:
    descriptor = Descriptor('descriptor')
    sub_descriptor = SubDescriptor('sub_descriptor')


client = ClientClass()
client.descriptor
client.descriptor = 'value'
client.sub_descriptor
client.sub_descriptor = 'value'

# Properties

class Property:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self
