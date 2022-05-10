from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 如果你想构造大量的结构体对象，你可以通过使用缓存来提升性能。
# 下面是一个例子：
import sys
import struct

def make_struct(fmt):
    return struct.Struct(fmt)

# Cache the Struct objects for fast reuse
_structs = make_struct('i?f')

class Structure:
    _fields_ = [
        ('integer', 'i'),
        ('boolean', '?'),
        ('floating', 'f')
    ]

    def __init__(self, integer, boolean, floating):
        self.integer = integer
        self.boolean = boolean
        self.floating = floating

