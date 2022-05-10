import bz2
bz2.BZ2File(filename, 'w')

# 写入压缩文件
with bz2.BZ2File(filename, 'w') as f:
    f.write(b'hello world')

# 读取压缩文件
with bz2.BZ2File(filename, 'r') as f:
    print(f.read())

# 压缩数据
data = bz2.compress(b'hello world')
print(data)

# 解压数据
print(bz2.decompress(data))

# 压缩级别
for i in range(1, 10):
    print('compress level', i, ':', len(bz2.compress(b'hello world', i)))

# 压缩级别
for i in range(1, 10):
    print('compress level', i, ':', len(bz2.
