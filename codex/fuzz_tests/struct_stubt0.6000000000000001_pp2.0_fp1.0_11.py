from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
print(s.size)

# 可以通过format字符串计算出结构所占的字节数。

# 通过format将元组转换成字节
packed_data = s.pack(b'abc', b'xyz', 1, 2)
print(packed_data)

# 解压
print(s.unpack(packed_data))

# 将代表位的元组转换成整数
def unpack_into(fmt, buf, offset=0):
    s = Struct(fmt)
    s.unpack_from(buf, offset)

# 下面是一些预定义的格式。
print(Struct('>I').pack(4))
print(Struct('<
