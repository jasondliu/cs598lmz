from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# Descriptor
class MyDescriptor:
    def __get__(self, obj, objtype):
        print('get')
        return 'mydescriptor'

class MyClass:
    mydescriptor = MyDescriptor()

MyClass.mydescriptor

# Metaclass
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

# Metaclass
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

# Metaclass
