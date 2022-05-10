from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('x')
s.pack(1)

class Structure:
    __slots__ = [
        '__weakref__', '_fields_',
        '__dict__', '__weakref__'
    ]

    def __init__(self):
        pass


class Stock(Structure):
    _fields_ = [
        ('name', str),
        ('shares', int),
        ('price', float)
    ]


class Point(Structure):
    _fields_ = [
        ('x', int),
        ('y', int)
    ]


class Address(Structure):
    _fields_ = [
        ('hostname', str),
        ('port', int),
        ('addr', Point)
    ]


__title__ = 'init.py'
__author__ = 'JieYuan'
__mtime__ = '19-3-18'

"""使用__slots__"""

# 类属性
# 类属性在类
