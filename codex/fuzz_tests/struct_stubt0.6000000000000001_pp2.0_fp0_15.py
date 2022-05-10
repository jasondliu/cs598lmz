from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<id")

data = s.pack(1, 2.0)
print(data)

# unpack
# < : little endian
# > : big endian
# b: signed char
# B: unsigned char
# h: short
# H: unsigned short
# i: int
# I: unsigned int
# l: long
# L: unsigned long
# f: float
# d: double

data = b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?'
print(s.unpack(data))

# 使用calcsize()

print(s.calcsize("<id"))

# 还有一种简便的方法是使用 struct.pack() 和 struct.unpack() 
# 两个函数直接执行打包和解包操作，
