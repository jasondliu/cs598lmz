from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize(s.format)

print(s.size)

# 创建一个结构体对象
import struct
st = struct.Struct('I 2s f')
print(st.size)

# 将结构体对象序列化
import struct
st = struct.Struct('I 2s f')
values = (1, b'ab', 2.7)
print(st.pack(*values))

# 将结构体对象反序列化
import struct
st = struct.Struct('I 2s f')
packed_data = st.pack(*(1, b'ab', 2.7))
print(st.unpack(packed_data))

# 将结构体对象写入文件
import struct
st = struct.Struct('
