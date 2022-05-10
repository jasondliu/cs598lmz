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


class Client:
    attr = Descriptor()


client = Client()
client.attr
client.attr = 'value'

# Metaclasses
class Meta(type):
    def __new__(cls, name, bases, body):
        print('Meta.__new__')
        return super().__new__(cls, name, bases, body)

    def __init__(self, name, bases, body):
        print('Meta.__init__')
        super().__init__(name, bases, body)


class Client(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Client.__new__')
        return
