from _struct import Struct
s = Struct.__new__(Struct)
s.size = 5
print(s)

s = Struct('i?f')
print(s.size)
#
#
#
# def func():
#     pass

# print (func())
# #
# #
# s = 'I love FishC.com!'
# print(s.isprintable())
# s = '\x08\x0c\n\r\t\v'
# print(s.isprintable())
# s = ''
# print(s.isprintable())
# #
# s = 'I love FishC.com!'
# print(s.endswith('FishC.com!'))
# # 从下标为8的字符开始判断
# print(s.endswith('love ',8,13))
# # 此时s一个字符都没有
# print(s.endswith('!',15,0))
