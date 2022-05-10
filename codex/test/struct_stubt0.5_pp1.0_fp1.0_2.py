from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# 使用关键字参数来构建结构
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(i=1, s=b'ab', f=2.7)

# 使用填充字符
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('x 2s f')
s.pack(b'ab', 2.7)
