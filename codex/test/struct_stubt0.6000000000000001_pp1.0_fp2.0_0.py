from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('HHI')
s.size

import ctypes
c_uint16 = ctypes.c_uint16
c_uint32 = ctypes.c_uint32

class Point(ctypes.Structure):
    _fields_ = [
        ('x', c_uint16),
        ('y', c_uint16),
        ('z', c_uint32),
    ]

p = Point(1, 2, 3)
p

p.x
p.y
p.z

# 列表中的元素都是Python对象，对列表的操作就是在操作这些对象。
# 如果你想要操作内存中的原始字节，你得先分配这些字节。
# 如果你想要在不
