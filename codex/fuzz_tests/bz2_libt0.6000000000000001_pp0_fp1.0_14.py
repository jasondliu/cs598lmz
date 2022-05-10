import bz2
bz2.BZ2File(path).read()

with bz2.BZ2File(path) as f:
    data = f.read()

with gzip.open(path, 'rb') as f:
    data = f.read()

with lzma.open(path) as f:
    data = f.read()

# 很多压缩文件都是二进制文件，因此需要使用rb模式来打开文件
# 如果文件不是二进制文件，那么可以不用指定模式
# 压缩的数据会被自动解码
# 写入的时候使用wb模式
# 如果需要
