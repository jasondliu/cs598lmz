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
        print('sub get')


class Client:
    descriptor = Descriptor('descriptor')
    sub_descriptor = SubDescriptor('sub_descriptor')


client = Client()
client.descriptor
client.sub_descriptor

# Metaclasses

class Meta(type):
    def __new__(cls, name, bases, body):
        print('Meta.__new__', cls, name, bases, body)
        if name == 'Base' and not body:
            return type.__new__(cls, name, bases, body)
