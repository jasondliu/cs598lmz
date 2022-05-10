from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = s.calcsize(s.format)
print(s.size)

# 通过给定的格式计算结构体的大小
print(Struct.calcsize('<3s3sHH'))

# 使用pack()方法将数据封装成结构体
packed_data = Struct.pack('<3s3sHH', b'\x12\x34\x56', b'\xab\xcd\xef', 1024, 2048)
print(packed_data)

# 使用unpack()方法将数据解封装成结构体
original_data = Struct.unpack('<3s3sHH', packed_data)
print(original_data)

# 使用unpack_from()方法将数据
