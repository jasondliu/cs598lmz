from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<I'
hex(s.unpack(s.pack(42))[0])

# struct.Struct.__new__(format)
# 创建一个Struct对象。format参数是一个字符串，用来创建该Struct对象的编码方法。它应该是一个标准的struct字符串参数，但是可以不包含字节长度。 如果有必要的话，字节长度可以通过使用sizeof()方法来计算。
# New in version 1.5.2.
print('New in version 1.5.2.\n')


# struct.Struct.__new__(cls, format)
print
