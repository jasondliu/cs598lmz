from _struct import Struct
s = Struct.__new__(Struct)
print(s)

# 实例化
s = Struct('i?f')
print(s.size)
print(s.pack(1, False, 3.14))
print(s.unpack(_))

# 定义一个结构体
class Point(Struct):
    _fields_ = [('x', c_int), ('y', c_int)]

p = Point(10, 20)
print(p.x, p.y)
print(p)

# 定义一个结构体
class PolyHeader(Struct):
    _fields_ = [('file_code', c_int32), ('min_x', c_double), ('min_y', c_double), ('max_x', c_double), ('max_y', c_double), ('num_polys', c_int32)]

# 读取文件
with open('../data/polys.bin', 'rb') as f:
    data = f.read
