from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你使用的是元类，那么你可以通过使用 __prepare__() 方法来自定义命名空间字典的创建。
# 下面是一个例子，它创建了一个有顺序的字典，并且在定义的时候自动插入了一些键值对：
from collections import OrderedDict
class Structure(object):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments

