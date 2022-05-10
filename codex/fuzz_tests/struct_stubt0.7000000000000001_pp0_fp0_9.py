from _struct import Struct
s = Struct.__new__(Struct)
print(s)
s.__init__('i?f')
print(s.size)
s.pack(1, False, 3.14159)

#  参数个数不匹配
#  s.pack(1, False, 3.14159, 42)

#  参数类型不匹配
#  s.pack(1, 2, 3)

import binascii
binascii.hexlify(s.pack(1, False, 3.14159))

#  读取时候的解包
s = Struct('i?f')
data = s.pack(1, False, 3.14159)
print(data)
s.unpack(data)

#  将结构体属性存储在字节字符串中，可以用_make()classmethod

s = Struct('
