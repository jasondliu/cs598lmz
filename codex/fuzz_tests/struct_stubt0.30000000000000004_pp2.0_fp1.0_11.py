from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

# 可以使用Struct对象的pack()和unpack()方法来打包和解包字节字符串
s.pack(1)
s.unpack(b'\x00\x01')

# 可以使用格式字符串'<HH'来描述一个结构，其中'<'表示小端法，'H'表示两个字节无符号整数
s = Struct('<HH')
s.size
s.pack(1,2)
s.unpack(b'\x01\x00\x02\x00')

# 可以使用格式字符串'<HH'来
