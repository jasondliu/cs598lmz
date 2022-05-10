from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>hhl')
s.pack(1,2,3)

class MyStruct(Struct):
    _fields = [('width', 'i'),
               ('height', 'i'),
               ('color', 'c')]

m = MyStruct.__new__(MyStruct)
m.__init__('>hhl')
m.pack(1,2,3)

#%%
import struct
class Structure:
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
        
