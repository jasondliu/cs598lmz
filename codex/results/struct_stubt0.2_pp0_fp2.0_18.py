from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# Descriptors

class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        print('get')

    def __set__(self, instance, value):
        print('set')


class SubDescriptor(Descriptor):
    def __get__(self, instance, cls):
        print('Sub get')


class ClientClass:
    descriptor = Descriptor('descriptor')
    sub_descriptor = SubDescriptor('sub_descriptor')


client = ClientClass()
client.descriptor
client.sub_descriptor

# Descriptor for handling attribute access

class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
       
