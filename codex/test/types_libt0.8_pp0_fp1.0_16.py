import types
types.MethodType(__init__, self)

class Spam(object):
    def __init__(self, name):
        self.name = name
s = Spam('Dave')
s.name

Spam.name = property(lambda self: self.__dict__['name'])

s.name


class Descriptor(object):

    def __get__(self, instance, instance_type):
        print('Getting', self, instance, instance_type)

    def __set__(self, instance, value):
        print('Setting', self, instance, value)

    def __delete__(self, instance):
        print('Deleting', self, instance)


class ClientClass(object):
    descriptor = Descriptor()


client = ClientClass()
client.descriptor

client.descriptor = 'value'
client.descriptor

del client.descriptor


class Descriptor(object):

    def __init__(self, name=None, **opts):
        self.name = name
