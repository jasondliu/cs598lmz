from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你想使用具名元组，并且需要更新某些属性的时候，可以使用命名元组实例的 _replace() 方法，它会创建一个全新的命名元组并将对应的字段用新的值取代。
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)
s

# 命名元组的一个主要用途是作为字典的替代，
