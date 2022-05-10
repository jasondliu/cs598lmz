from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s = Struct.__new__(Struct, 'i')
s.size

Struct.__new__(Struct, 'i', 'j')

import sys
if sys.maxsize > 2**32:
    # 64-bit only
    Struct.__new__(Struct, 'q')
    Struct.__new__(Struct, 'q', 'q')

class A(object):
    pass
a = A()
# no __init__
Struct.__new__(Struct, 'i', a)
# wrong number of arguments
Struct.__new__(Struct, 'i', a, a)
