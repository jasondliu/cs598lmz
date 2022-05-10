from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# _struct can pack and unpack bytes
data = s.pack(1, 'ab'.encode('utf-8'), 2.7)
s.unpack(data)

# _struct can be used in memoryview
m1 = memoryview(data)
m2 = m1.cast('I')
m2.tolist()

# _struct can be used in array
from array import array
numbers = array('f', (1.0, 1.5, 2.0, 2.5))
s = Struct.__new__(Struct)
s.__init__('f')
s.pack_into(numbers, 0, 3.14159)
numbers

# _struct can be used in ctypes
from ctypes import Structure, c_float
class Point(Structure):
    _fields_ = [('x', c_float), ('y', c_float)]
