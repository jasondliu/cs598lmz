from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = '<3s3sHH'
print(s.size)

# 可以通过使用新的关键字参数来创建结构体实例
import time, struct
print(struct.pack('>I', 10240099))
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

# 格式化
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 
