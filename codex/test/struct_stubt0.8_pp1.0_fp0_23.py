from _struct import Struct
s = Struct.__new__(Struct)
s.__doc__ 
print(s.__doc__)

# 重载__new__ 方法
class Structure:
    _fields = []
    
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fileds)))
        
        # Set the argument
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    
s1 = Stock('ACME', 50, 91.1)
s2 = Stock('ACME', 50)

# 我们可以用一个特殊的私有属性_fields 来记录这个类的字段名称。然后，在构造函
