from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# test __new__ on a metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        return type.__new__(cls, name, bases, dct)

class C(object):
    __metaclass__ = Meta

# test __new__ on a metaclass with a __call__
class Meta(type):
    def __new__(cls, name, bases, dct):
        return type.__new__(cls, name, bases, dct)
    def __call__(self, *args):
        return self.__new__(self, *args)

class C(object):
    __metaclass__ = Meta

# test __new__ on a metaclass with a __call__ that takes keyword args
class Meta(type):
    def __new__(cls, name, bases, dct):
        return type.__new__(cls, name, bases, dct)
    def __call
