from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
print(s.size)
print(s.pack(b'\x01', b'\x02', 0x1234, 0x5678))
print(s.unpack(b'\x01\x02\x12\x34\x56\x78'))

# _struct.Struct.pack(format, v1, v2, ...)
# _struct.Struct.unpack(buffer)

# 定义一个结构体类
# class Structure:
#     _fields_ = []
#     def __init__(self, *args, **kwargs):
#         for name, fmt in self._fields_:
#             setattr(self, name, args[i])

#     def pack(self):
#         pass

#     def unpack(self):
#         pass

