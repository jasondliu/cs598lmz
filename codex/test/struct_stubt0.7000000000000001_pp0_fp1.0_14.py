from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(1) #首先初始化对象s
s.__setattr__('format', 'I')
s.__getattribute__('size')

class Struct(object):
    def __init__(self, format):
        self.__format = format
    def size(self):
        return Struct.__calcsize(self.__format)
Struct.__new__ = lambda cls, *args: object.__new__(cls)
Struct.__calcsize = _struct.calcsize
Struct.__getattribute__ = lambda self, name: object.__getattribute__(self,name) if name != 'size' else self.size()
s = Struct('I')
s.size()
s.__getattribute__('size')
s.__getattribute__('__format')

