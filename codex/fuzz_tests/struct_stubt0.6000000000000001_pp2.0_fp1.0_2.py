from _struct import Struct
s = Struct.__new__(Struct)
print(s.unpack('<5s5s5s5s', b'ABCDEabcdeabcdeabcdeabcde'))

# 使用*号支持任意多的字段
print(Struct('<4s').unpack(b'abcd'))
print(Struct('<4s4s').unpack(b'abcdabcd'))
print(Struct('<4s4s4s').unpack(b'abcdabcdabcd'))

# 使用?表示一个空的占位符
print(Struct('<?3s').unpack(b'abc'))
print(Struct('<?3s').pack(b'abc'))

# 格式符号
# b: 一个有符号字节
# B: 一个无符号字节
# h: 一个有符号
