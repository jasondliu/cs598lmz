from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)
print(s.pack(1))
print(s.unpack(b'\x01\x00\x00\x00'))

# class Struct(format, ...):
#     def __init__(self, format, ...):
#         pass
#     def pack(*args):
#         pass
#     def unpack(buffer):
#         pass
#     def pack_into(buffer, offset, *args):
#         pass
#     def unpack_from(buffer, offset=0):
#         pass
#     def calcsize():
#         pass


# 字符串格式化

# 字符串格式化有三种方式：
# 第一种方式：
print('%s is %d years old.' % ('Bob', 19))
# 第二种方式：
print('{0} is {1
