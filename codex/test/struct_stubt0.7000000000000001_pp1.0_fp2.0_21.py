from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 4s f'
s.size = 16
print(s.size)
print('s.format:', s.format)
print(s.unpack(b'\x08\x00\x00\x00spam\x00\x00\xae\x7f'))

# Example: Using a Named Struct Subclass
class Structure(Struct):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
class Stock(Structure):
    _fields = ['name', 'shares', 'price']
