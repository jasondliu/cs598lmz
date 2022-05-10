from _struct import Struct
s = Struct.__new__(Struct)
print(s)
s.__init__('2x 3x')
print(s.size)
print(help(s.pack_into))

'''
class array.array(typecode[, initializer])
'''
from array import array
print(dir(array))
from pprint import pprint
a = array('l')
print(a)
print(a.append(2))
print(a.append(4))
print(a.append(5))
print(a.pop())
print(a.pop(0))
print(a.pop())
print(a.append(8))
print(a)
b = array('f', (2.1, 3.4, 4.6, 8.1))
print(b)
'''
class array.array(typecode[, initializer])
'''
from array import array
print(dir(array))
from pprint import pprint
a = array('l')
print(a)
print(a.append(2))
print(a.append(4))
