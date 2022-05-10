from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size
s.pack(1, False, 3.14)

# 使用类来实现结构体
class Structure:
    _fields_ = []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields_):
            raise TypeError('Expected {} arguments'.format(len(self._fields_)))
        # Set the arguments
        for name, value in zip(self._fields_, args):
            setattr(self, name, value)
        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields_
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))

class Stock(Structure):
    _fields_ = ['name', 'shares', 'price']
