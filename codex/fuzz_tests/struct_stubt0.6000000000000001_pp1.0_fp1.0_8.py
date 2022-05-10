from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>3s3sHH'
print(len(s.pack('abc', 'abcd', 'abcd', 1, 2)))

# 只有元组，列表，字典，集合，即不可变的数据类型可以hash
# print(hash(s))

# 元组的hash值是每一个元素的hash值的异或运算
# 集合的hash值是每一个元素的hash值的或运算
# 列表的hash值是每一个元素的hash值的与运算
# 字典的hash值是每一个键的hash值的与运算
