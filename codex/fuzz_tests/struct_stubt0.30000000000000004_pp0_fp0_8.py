from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# Descriptors

class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        print('__get__', self, instance, cls)

    def __set__(self, instance, value):
        print('__set__', self, instance, value)

    def __delete__(self, instance):
        print('__delete__', self, instance)

class ClientClass:
    descriptor = Descriptor('descriptor')

client = ClientClass()
client.descriptor
client.descriptor = 'value'
del client.descriptor

# Descriptor for handling attribute access

class Typed:
    _expected_type = type(None)
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set
