from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>2h'
s.size = 8
print(s.unpack(b'\x00\x01\x00\x02'))

# 可以通过继承来创建子类，从而增加新的方法
class Structure(Struct):
    def __init__(self, format, *args):
        super().__init__(format)
        self._fields = args
    def __iter__(self):
        for name in self._fields:
            yield name

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

s = Stock('ACME', 50, 91.1)
print(s)
print(s.name)
print(s.shares)
print(s.price)

# 如果你想通过某个元素的值来访问它，可
