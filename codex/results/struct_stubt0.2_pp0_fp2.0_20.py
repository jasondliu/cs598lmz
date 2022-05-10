from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = calcsize(s.format)

with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
print(s.unpack(header))
del header
del s

# 文件对象支持使用标准的索引和切片操作。
# 切片的结果是一个类似数组的对象，它包含原始数据的一个片段。
# 如果你需要修改这个片段，那么你需要使用切片赋值或者使用 by
