from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# test that we can use a custom metaclass
class MyMeta(type):
    pass

class MyClass(object):
    __metaclass__ = MyMeta

# test that we can use a custom metaclass with __prepare__
class MyMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return {}

class MyClass(object):
    __metaclass__ = MyMeta

# test that we can use a custom metaclass with __new__
class MyMeta(type):
    def __new__(metacls, name, bases, namespace, **kwds):
        return super().__new__(metacls, name, bases, namespace)

class MyClass(object):
    __metaclass__ = MyMeta

# test that we can use a custom metaclass with __init__
class MyMeta(type):
    def __init__(cls, name, bases, namespace, **kwds):
