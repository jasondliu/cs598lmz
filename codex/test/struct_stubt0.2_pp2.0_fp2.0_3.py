from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 使用__new__方法创建的实例，调用__init__方法时，会传入self参数
# 使用__new__方法创建的实例，调用__init__方法时，会传入self参数

# 创建一个类，它的实例拥有一个名为name的属性
class Structure:
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

#
