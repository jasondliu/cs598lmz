from _struct import Struct
s = Struct.__new__(Struct)
s.format = '3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(s.unpack(header))
del header
del s

# 内存视图的切片只是原始缓冲区的一个视图，并不会复制任何数据。
# 因此，切片后的内存视图与原始内存视图共享相同的底层缓冲区，修改其中一个会影响到另一个

# 内存视图可以被看作是 NumPy 数组，因此
